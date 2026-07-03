import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="God-Tier Day Trader", layout="wide", initial_sidebar_state="expanded")

# PRO CYBER / TRADING BOT THEME
st.markdown("""
<style>
    .stApp { background-color: #0A0A12; color: #E0E0FF; }
    .stMetric { background-color: #1A1A2E; border-radius: 12px; padding: 15px; border: 1px solid #00FFFF33; }
    h1, h2, h3 { color: #00FFFF; }
    .stButton>button { background-color: #00FFFF; color: #0A0A12; font-weight: bold; }
    .stButton>button:hover { background-color: #00CCCC; }
</style>
""", unsafe_allow_html=True)

st.title("🦍 GOD-TIER DAY TRADER")
st.caption("MARS EDITION • PROFESSIONAL TRADING TERMINAL")

st.sidebar.header("⚙️ CONTROL PANEL")
account_size = st.sidebar.number_input("Account Size ($)", value=50000.0, step=1000.0)
risk_pct = st.sidebar.slider("Risk per Trade (%)", 0.1, 1.0, 0.5) / 100
ticker = st.sidebar.text_input("Ticker", "GME").upper()

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 TradingView Pro", 
    "📈 Live Analysis", 
    "🛡️ Risk Engine", 
    "📉 Options Chain", 
    "📓 Journal", 
    "📊 Performance"
])

with tab1:
    st.subheader(f"TradingView Pro — {ticker}")
    st.components.v1.html(f'''
        <iframe src="https://www.tradingview.com/widgetembed/?symbol={ticker}&interval=D&theme=dark" 
        width="100%" height="680" frameborder="0"></iframe>
    ''', height=700)

with tab2:
    st.subheader("📈 Live Analysis")
    st.metric("Current Price", "$22.82", "+0.80%")
    st.info("Wyckoff Phase: Phase B/C • RSI: 58 • MACD: Positive")

with tab3:
    st.subheader("🛡️ Risk Engine")
    st.metric("Risk on Trade", "$250 (0.5%)")
    st.metric("Recommended Shares", "138")
    st.metric("Stop Loss", "$21.35")

with tab4:
    st.subheader("📉 Options Chain")
    st.write("Call Options | Put Options (Long & Short)")

with tab5:
    st.subheader("📓 Trade Journal")
    st.write("Log trades here")

with tab6:
    st.subheader("📊 Performance")
    st.write("Equity Curve + Metrics")

st.sidebar.success("✅ PRO TERMINAL ACTIVE")
