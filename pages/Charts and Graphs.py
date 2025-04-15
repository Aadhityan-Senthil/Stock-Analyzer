import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

# Title
st.title("📊 Stock Chart")

# Input
symbol = st.text_input("Enter Stock Symbol", "AAPL")
start_date = st.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("2025-04-15"))

@st.cache_data
def fetch_stock_data(symbol, start, end):
    try:
        # Fetch data
        data = yf.download(symbol, start=start, end=end)
        
        # Check if the data is in MultiIndex format
        if isinstance(data.columns, pd.MultiIndex):
            # Flatten the MultiIndex
            data.columns = [' '.join(col).strip() for col in data.columns.values]
        
        # Reset index to ensure 'Date' is a column
        data.reset_index(inplace=True)

        # Normalize column names (strip leading/trailing whitespaces, lower case, etc.)
        data.columns = data.columns.str.strip().str.lower()

        # Ensure 'Date' column is in datetime format
        data['date'] = pd.to_datetime(data['date'])

        # Print column names and first few rows for debugging
        st.write("Columns in the DataFrame:", data.columns)
        st.write("First few rows of the DataFrame:", data.head())

        return data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()

if st.button("Show Chart"):
    df = fetch_stock_data(symbol, start_date, end_date)

    if df.empty:
        st.error(f"Failed to fetch data for {symbol}. Please check the symbol or date range.")
    else:
        st.subheader(f"{symbol} Stock Price Chart")

        # Use the full column name for closing price including the symbol ('close aapl')
        fig = px.line(df, x='date', y=f'close {symbol.lower()}', title=f"{symbol} Closing Price")
        st.plotly_chart(fig, use_container_width=True)

        # Optional: show OHLC or volume
        with st.expander("Show Raw Data & Other Charts"):
            st.dataframe(df)

            fig2 = px.line(df, x='date', y=[f'open {symbol.lower()}', f'high {symbol.lower()}', f'low {symbol.lower()}', f'close {symbol.lower()}'], title=f"{symbol} OHLC")
            st.plotly_chart(fig2, use_container_width=True)

            fig3 = px.bar(df, x='date', y=f'volume {symbol.lower()}', title=f"{symbol} Volume")
            st.plotly_chart(fig3, use_container_width=True)
