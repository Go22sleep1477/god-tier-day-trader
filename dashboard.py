import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="God-Tier Day Trader", layout="wide", initial_sidebar_state="expanded")
st.title("🦍 God-Tier Day Trader — Professional Terminal")

# Dark Theme
st.markdown("""
<style>
    .stApp { background-color: #0E1117; color: #FAFAFA; }
    .css-1d391kg { background-color: #1E1E1E; }
</style>
""", unsafe_allow_html=True)

st.sidebar.header("⚙️ Control Panel")
account_size = st.sidebar.number_input("Account Size ($)", value=50000.0, step=1000.0)
risk_pct = st.sidebar.slider("Risk %", 0.1, 1.0, 0.5) / 100
ticker = st.sidebar.text_input("Main Ticker", "GME").upper()

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 TradingView", 
    "📈 Live Market", 
    "🧠 Risk & Sizing", 
    "📓 Journal", 
    "🤖 Hermes AI"
])

with tab1:
    st.subheader(f"TradingView — {ticker}")
    st.components.v1.html(f'''
        <iframe src="https://www.tradingview.com/widgetembed/?symbol={ticker}&interval=D&theme=dark&style=1" 
        width="100%" height="700" frameborder="0"></iframe>
    ''', height=720)

with tab2:
    st.subheader("Live Market Data")
    st.info("Alpaca + Real-time data coming after you add keys")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Last Price", "22.82", "+0.18 (+0.80%)")
    with col2:
        st.metric("Volume", "4.57M", "↑")

with tab3:
    st.subheader("Risk & Position Sizing")
    entry = st.number_input("Entry Price", value=22.75)
    atr = st.number_input("ATR", value=1.8)
    mult = st.select_slider("Stop Multiplier", [1.0, 1.5, 2.0, 2.5], value=1.5)
    
    stop = round(entry - (atr * mult), 2)
    risk_amount = round(account_size * risk_pct, 2)
    shares = int(risk_amount / (entry - stop)) if (entry - stop) > 0 else 0
    
    st.metric("Recommended Shares", shares)
    st.metric("Stop Loss", f"${stop}")
    st.metric("Risk Amount", f"${risk_amount} ({risk_pct*100:.1f}%)")

with tab4:
    st.subheader("Trade Journal")
    st.write("Log your trades here (will be saved)")

with tab5:
    st.subheader("Hermes AI Prompts")
    st.write("Copy these into Hermes Agent")

st.sidebar.success("✅ Professional Mode Active")
