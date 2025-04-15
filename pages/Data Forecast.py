import streamlit as st
import pandas as pd 
from utils import fetch_stock_data

st.set_page_config(page_title="Stock Dashboard", layout="wide")
st.title("📊 Real-Time Stock Dashboard")

symbol = st.text_input("Enter stock symbol (e.g., AAPL)", "AAPL")
start_date = st.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", value=pd.to_datetime("today"))

if symbol:
    data = fetch_stock_data(symbol, start_date, end_date)
    if data.empty:
        st.error("Failed to fetch data. Please check symbol or date range.")
    else:
        st.session_state["symbol"] = symbol
        st.session_state["start_date"] = start_date
        st.session_state["end_date"] = end_date
        st.session_state["data"] = data
        st.success(f"Data for {symbol} loaded successfully!")
        st.dataframe(data.tail())
