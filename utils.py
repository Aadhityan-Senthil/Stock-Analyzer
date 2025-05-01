import yfinance as yf
import pandas as pd
import numpy as np
import requests
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import streamlit as st

@st.cache_data(ttl=3600)
def fetch_stock_data(symbol, start, end):
    from datetime import datetime

    # Ensure end date is not in the future
    today = datetime.today().strftime('%Y-%m-%d')
    if end > today:
        end = today

    try:
        df = yf.download(symbol, start=start, end=end)
        return df if not df.empty else pd.DataFrame()
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()

def fetch_news(symbol):
    key = st.secrets["newsapi"]["api_key"]
    url = f"https://newsapi.org/v2/everything?q={symbol}&sortBy=publishedAt&apiKey={key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("articles", [])[:5]
    return []

def add_moving_average(df, window):
    df["MA"] = df["Close"].rolling(window).mean()
    return df

def add_ema(df, span):
    df["EMA"] = df["Close"].ewm(span=span, adjust=False).mean()
    return df

def add_bollinger_bands(df, window=20, num_std_dev=2):
    rolling_mean = df['Close'].rolling(window).mean()
    rolling_std = df['Close'].rolling(window).std()
    df['Upper'] = rolling_mean + (rolling_std * num_std_dev)
    df['Lower'] = rolling_mean - (rolling_std * num_std_dev)
    return df

def add_rsi(df, window=14):
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df

def add_macd(df):
    exp1 = df['Close'].ewm(span=12, adjust=False).mean()
    exp2 = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = exp1 - exp2
    df['Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
    return df

def detect_anomalies(df):
    model = IsolationForest(contamination=0.05)
    df["Anomaly"] = model.fit_predict(df[["Close"]])
    return df
