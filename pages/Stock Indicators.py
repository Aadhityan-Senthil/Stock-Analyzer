import streamlit as st
import pandas as pd
import yfinance as yf

# Function to compute RSI
def compute_rsi(df, close_col='Close', window=14):
    delta = df[close_col].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    df['RSI'] = rsi
    return df

# Function to compute MACD
def compute_macd(df, close_col='Close'):
    exp1 = df[close_col].ewm(span=12, adjust=False).mean()
    exp2 = df[close_col].ewm(span=26, adjust=False).mean()
    macd = exp1 - exp2
    signal = macd.ewm(span=9, adjust=False).mean()
    df['MACD'] = macd
    df['MACD_Signal'] = signal
    return df

# Function to compute Moving Averages
def compute_moving_averages(df, close_col='Close'):
    df['MA_20'] = df[close_col].rolling(window=20).mean()
    df['MA_50'] = df[close_col].rolling(window=50).mean()
    return df

# Fetch stock data
@st.cache_data
def fetch_stock_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [' '.join(col).strip() for col in data.columns.values]
    return data

# UI
st.title("📊 Stock Indicators")

symbol = st.text_input("Enter Stock Symbol", "AAPL")
start_date = st.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("2025-04-15"))

indicators = st.multiselect(
    "Select Indicators to Display",
    ["RSI", "MACD", "Moving Averages"],
    default=["RSI"]
)

if st.button("Fetch Data"):
    df = fetch_stock_data(symbol, start_date, end_date)

    if not df.empty:
        df = df.reset_index()
        close_col = next((col for col in df.columns if 'close' in col.lower()), None)

        if close_col:
            st.subheader(f"Indicators for {symbol}")
            
            # RSI
            if "RSI" in indicators:
                df = compute_rsi(df, close_col=close_col)
                st.line_chart(df.set_index('Date')[['RSI']])
                
                latest_rsi = df['RSI'].dropna().iloc[-1]
                st.markdown(f"**Latest RSI:** {latest_rsi:.2f}")
                if latest_rsi > 70:
                    st.warning("⚠️ The stock is **Overbought** (RSI > 70). Consider caution.")
                elif latest_rsi < 30:
                    st.success("✅ The stock is **Oversold** (RSI < 30). Potential buying opportunity.")
                else:
                    st.info("ℹ️ The stock is in a **Neutral** RSI range (30–70).")

            # MACD
            if "MACD" in indicators:
                df = compute_macd(df, close_col=close_col)
                st.line_chart(df.set_index('Date')[['MACD', 'MACD_Signal']])

                latest_macd = df['MACD'].dropna().iloc[-1]
                latest_signal = df['MACD_Signal'].dropna().iloc[-1]
                st.markdown(f"**Latest MACD:** {latest_macd:.2f}, **Signal Line:** {latest_signal:.2f}")
                if latest_macd > latest_signal:
                    st.success("📈 **Bullish Signal**: MACD is above the signal line.")
                else:
                    st.warning("📉 **Bearish Signal**: MACD is below the signal line.")

            # Moving Averages
            if "Moving Averages" in indicators:
                df = compute_moving_averages(df, close_col=close_col)
                st.line_chart(df.set_index('Date')[[close_col, 'MA_20', 'MA_50']])

                latest_close = df[close_col].iloc[-1]
                latest_ma20 = df['MA_20'].iloc[-1]
                latest_ma50 = df['MA_50'].iloc[-1]

                st.markdown(f"**Latest Close:** {latest_close:.2f} | MA20: {latest_ma20:.2f} | MA50: {latest_ma50:.2f}")
                if latest_close > latest_ma20 and latest_close > latest_ma50:
                    st.success("📈 Price is above both MA20 and MA50: **Bullish Trend**")
                elif latest_close < latest_ma20 and latest_close < latest_ma50:
                    st.warning("📉 Price is below MA20 and MA50: **Bearish Trend**")
                else:
                    st.info("ℹ️ Price is in a mixed zone between MA20 and MA50.")

        else:
            st.error("Close column not found.")
    else:
        st.error("No data found for the given symbol and date range.")
