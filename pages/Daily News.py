import streamlit as st
import pandas as pd 
from utils import fetch_news

st.title("📰 Latest Stock News")

if "symbol" not in st.session_state:
    st.warning("Select a stock on the Home page.")
else:
    symbol = st.session_state["symbol"]
    articles = fetch_news(symbol)
    if not articles:
        st.error("Could not fetch news.")
    else:
        for article in articles:
            st.subheader(article["title"])
            st.write(article["description"])
            st.markdown(f"[Read more]({article['url']})")
            st.markdown("---")
