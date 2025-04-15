import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px

st.title("🚨 Anomaly Detection")

symbol = st.text_input("Enter Stock Symbol", "AAPL").upper()
start_date = st.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("today"))

if symbol and start_date and end_date:
    try:
        df = yf.download(symbol, start=start_date, end=end_date, group_by='ticker')

        if df.empty:
            st.error(f"No data found for {symbol}. Try another symbol or date range.")
        else:
            # Reset index to bring 'Date' as a column
            df = df.reset_index()

            # If multi-indexed columns, flatten them
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = ['_'.join([str(i) for i in col if i]) for col in df.columns]

            # Find the appropriate close column (e.g., Close_AAPL or Close)
            close_col = None
            for col in df.columns:
                if "Close" in col and symbol in col:
                    close_col = col
                    break
            if not close_col and "Close" in df.columns:
                close_col = "Close"

            if not close_col:
                st.error(f"Could not find Close price column in data. Available columns: {df.columns}")
            else:
                # Anomaly detection based on z-score
                mean = df[close_col].mean()
                std = df[close_col].std()
                df['Anomaly'] = np.where(abs((df[close_col] - mean) / std) > 2, df[close_col], np.nan)

                fig = px.line(df, x="Date", y=close_col, title=f"{symbol} Close Price with Anomalies")
                fig.add_scatter(x=df["Date"], y=df["Anomaly"], mode="markers", name="Anomalies", marker=dict(color="red", size=8))
                st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"An error occurred: {e}")
