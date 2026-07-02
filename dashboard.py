import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="God-Tier Day Trader", layout="wide")
st.title("🦍 God-Tier Day Trader — Professional Edition")

st.sidebar.header("Settings")
account_size = st.sidebar.number_input("Account Size ($)", value=50000.0, step=1000.0)
risk_pct = st.sidebar.slider("Risk per Trade (%)", 0.1, 1.0, 0.5) / 100

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 TradingView", 
    "📈 Alpaca Live", 
    "🧮 Risk Calculator", 
    "📝 Journal", 
    "🤖 Hermes Prompts"
])

with tab1:
    st.subheader("TradingView Charts")
    ticker = st.text_input("Symbol", "NVDA").upper()
    st.components.v1.html(f'''
        <iframe src="https://www.tradingview.com/widgetembed/?symbol={ticker}&interval=D&theme=dark" 
        width="100%" height="600" frameborder="0"></iframe>
    ''', height=650)

with tab2:
    st.subheader("Alpaca Analysis")
    st.info("Add your Alpaca keys in Streamlit Secrets to enable live data")

with tab3:
    st.subheader("Risk Calculator")
    st.write("Volatility-adjusted risk tools will appear here")

with tab4:
    st.subheader("Trade Journal")
    st.write("Journal coming soon")

with tab5:
    st.subheader("Hermes Prompts")
    st.write("Ready prompts will be here")

st.sidebar.success("✅ Full Version Loaded")
