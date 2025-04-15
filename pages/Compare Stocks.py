import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Set page config at the top
st.set_page_config(page_title="Compare Stocks", layout="wide")

# Title
st.title("📈 Compare Multiple Stocks")

# Sidebar inputs
with st.sidebar:
    st.header("Stock Comparison Settings")
    symbols_input = st.text_input("Enter stock symbols (comma separated)", "AAPL, MSFT, GOOGL")
    start_date = st.date_input("Start Date", pd.to_datetime("2023-01-01"))
    end_date = st.date_input("End Date", pd.to_datetime("today"))

# Process input symbols
symbols_list = [s.strip().upper() for s in symbols_input.split(",") if s.strip()]

# Validate symbols
if len(symbols_list) < 2:
    st.warning("Please enter at least 2 valid stock symbols to compare.")
    st.stop()

# Fetch data
@st.cache_data
def fetch_stock_data(symbol, start, end):
    try:
        df = yf.download(symbol, start=start, end=end)
        df["Symbol"] = symbol
        return df
    except Exception as e:
        st.error(f"Failed to fetch data for {symbol}: {e}")
        return pd.DataFrame()

# Gather all stock data
data_frames = [fetch_stock_data(symbol, start_date, end_date) for symbol in symbols_list]
data = pd.concat(data_frames)

# Check if data is valid
if data.empty:
    st.error("No data found for the given symbols and date range.")
    st.stop()

# Reset index and prepare for plotting
data.reset_index(inplace=True)

# Plot using Plotly
fig = go.Figure()
for symbol in symbols_list:
    symbol_df = data[data["Symbol"] == symbol]
    fig.add_trace(go.Scatter(
        x=symbol_df["Date"],
        y=symbol_df["Close"],
        mode='lines',
        name=symbol
    ))

fig.update_layout(
    title="Stock Closing Price Comparison",
    xaxis_title="Date",
    yaxis_title="Closing Price (USD)",
    template="plotly_dark",
    height=600,
)

st.plotly_chart(fig, use_container_width=True)

# Show table
st.subheader("📄 Raw Data (Last 5 Days per Stock)")
latest_data = data.groupby("Symbol").apply(lambda x: x.tail(5)).reset_index(drop=True)
st.dataframe(latest_data)
