import streamlit as st

# Set page config at the very beginning
st.set_page_config(page_title="Home - Stock Dashboard", layout="wide")

# Inject custom CSS
st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: #ffffff;
        font-family: 'Helvetica Neue', sans-serif;
    }

    .center {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        justify-content: center;
    }

    .big-title {
        font-size: 3em;
        font-weight: bold;
        color: #08fdd8;
        margin-bottom: 0.5em;
    }

    .card {
        background-color: #1e1e1e;
        padding: 1.5em;
        border-radius: 12px;
        margin: 1em 0;
        box-shadow: 0 0 15px rgba(8, 253, 216, 0.2);
        max-width: 900px;
        width: 100%;
    }

    .section-image {
        max-width: 500px;
        border-radius: 12px;
        margin: 1em 0;
        box-shadow: 0 0 15px rgba(8, 253, 216, 0.1);
    }

    .flex-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 2em;
        margin-top: 1.5em;
    }

    .footer {
        margin-top: 3em;
        font-size: 0.85em;
        color: gray;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<div class="center">', unsafe_allow_html=True)
st.markdown('<div class="big-title">📈 Welcome to the Real-Time Stock Analysis Dashboard</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Section 1: Introduction
st.markdown("""
## 🔍 What is this?
A portfolio-ready **stock analysis tool** built with **Streamlit**. Designed to give investors, traders, and enthusiasts everything they need to analyze the stock market in one interactive place.

### ⚡ Key Features:
- **Historical Stock Data**: Get detailed stock data for any company and visualize its performance over time. View historical trends in interactive charts for clear insights into past market movements.
- **Technical Indicators**: Enhance your analysis with popular technical indicators like **RSI**, **MACD**, and **Moving Averages**. These indicators can help identify potential buy/sell signals and predict market trends.
- **Anomaly Detection**: Identify unusual market movements that could represent potential opportunities or risks. Using advanced algorithms, the dashboard detects anomalies in stock prices, enabling smarter decisions.
- **Real-Time News**: Stay on top of market developments with up-to-date financial news. By integrating news APIs, the dashboard keeps you informed on the latest headlines that could affect stock prices and market trends.
- **Compare Stocks**: The **Compare Page** allows you to analyze multiple stock symbols side-by-side. This feature lets users visually compare historical trends, price movements, and volume of different companies, enabling deeper insights and more informed investment decisions.            
- **Modern UI**: The sleek and intuitive design allows both beginners and experienced traders to interact with stock data effortlessly. You don’t need to be a financial expert to understand the key insights the dashboard provides.
- **Beginner Friendly**: Tailor your stock analysis experience with customizable settings, letting you focus on what matters most to your trading strategy.

Make data-driven decisions confidently, whether you're just getting started or optimizing your trading strategy.
""")

# Section 2: Purpose of the Project
st.markdown('<div class="flex-container">', unsafe_allow_html=True)
st.markdown(f"""
    <div style="flex: 1; padding-right: 20px;">
        <h2>🎯 Purpose of the Project</h2>
        <p>This project offers a user-friendly platform for analyzing stock market data, combining key features to help traders and investors make informed decisions:</p>
        <ul>
            <li><strong>Bridge the gap between data and insights</strong>: Turn raw stock data into actionable information.</li>
            <li><strong>Explore technical indicators visually</strong>: Visualize RSI, MACD, and moving averages to identify trends and signals.</li>
            <li><strong>Anomaly detection</strong>: Spot irregular price behavior and potential opportunities or risks.</li>
            <li><strong>Stay informed with market news</strong>: Keep up with the latest news that could impact stock prices.</li>
        </ul>
        <p>Built with real-time APIs and modular code, this project demonstrates a powerful yet flexible dashboard for financial analysis.</p>
    </div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Section 3: Built To Demonstrate
st.markdown("""
### 🛠️ Built to Demonstrate
- 📡 **Real-time API integration**: Access the latest stock data via real-time APIs.
- 📊 **Interactive charts**: Visualize stock performance and trends with interactive Plotly charts.
- 🧩 **Modular structure**: The code is organized for easy updates and feature additions.
- ⚙️ **Performance optimization**: Designed to provide a smooth user experience even with large datasets.
""")

# Section 4: Page Guide
st.markdown('<div class="flex-container">', unsafe_allow_html=True)
st.markdown(f"""
    <div style="flex: 1; padding-left: 20px;">
        <h2>🧭 Page Guide</h2>
        <ul>
            <li><strong>Home</strong>: Overview of the dashboard and its purpose</li>
            <li><strong>Data Loader</strong>: Choose stock symbols and date ranges</li>
            <li><strong>Charts</strong>: Explore trends, candlesticks, and volume</li>
            <li><strong>Indicators</strong>: Dive into RSI, MACD, and Moving Averages</li>
            <li><strong>Compare</strong>: Compare stocks trends and volume for better insights.</li>
            <li><strong>Anomalies</strong>: Detect spikes and irregular price patterns</li>
            <li><strong>News</strong>: Stay informed with integrated financial headlines</li>
            <li><strong>Compare</strong>: Compare multiple stocks side-by-side</li>
        </ul>
    </div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Made with ❤️ using Streamlit</div>', unsafe_allow_html=True)
