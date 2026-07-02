import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="God-Tier Day Trader", layout="wide", initial_sidebar_state="expanded")

# Dark Professional Theme
st.markdown("""
<style>
    .stApp { background-color: #0E1117; color: #FAFAFA; }
    .metric-card { background-color: #1E1E1E; padding: 15px; border-radius: 10px; }
    h1, h2, h3 { color: #FAFAFA; }
</style>
""", unsafe_allow_html=True)

st.title("🦍 God-Tier Day Trader — Professional Terminal")

# Sidebar
st.sidebar.header("⚙️ Control Panel")
account_size = st.sidebar.number_input("Account Size ($)", value=50000.0, step=1000.0)
risk_pct = st.sidebar.slider("Risk per Trade (%)", 0.1, 1.0, 0.5) / 100
ticker = st.sidebar.text_input("Ticker", "GME").upper()

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 TradingView", 
    "📈 Market Structure", 
    "🧠 Risk & Sizing", 
    "📓 Journal", 
    "🤖 Hermes Prompts"
])

with tab1:
    st.subheader(f"TradingView Chart — {ticker}")
    st.components.v1.html(f'''
        <iframe src="https://www.tradingview.com/widgetembed/?symbol={ticker}&interval=D&theme=dark&style=1" 
        width="100%" height="720" frameborder="0"></iframe>
    ''', height=740)

with tab2:
    st.subheader("Market Structure & Key Levels")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Current Price", "$22.82", "+0.80%")
    with col2:
        st.metric("Recent High", "$26.50")
    with col3:
        st.metric("Recent Low", "$23.00")
    
    st.write("**Market Structure:** Consolidation / Base Building")
    st.write("**Key Resistance:** $26.00 – $26.50")
    st.write("**Key Support:** $23.00 – $23.50")
    st.write("**Candle Pattern:** Solid green candle with healthy volume on latest session")

with tab3:
    st.subheader("Volatility-Adjusted Risk & Position Sizing")
    entry = st.number_input("Planned Entry", value=22.82)
    atr = st.number_input("Estimated ATR", value=1.8)
    mult = st.select_slider("ATR Multiplier", [1.0, 1.5, 2.0, 2.5], value=1.5)
    
    stop_dist = round(atr * mult, 2)
    risk_amount = round(account_size * risk_pct, 2)
    shares = int(risk_amount / stop_dist) if stop_dist > 0 else 0
    target = round(entry + (stop_dist * 2), 2)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Stop Distance", f"${stop_dist}")
    col2.metric("Shares", shares)
    col3.metric("Risk Amount", f"${risk_amount}")
    st.success(f"**1:2 Target:** ${target}")

with tab4:
    st.subheader("Trade Journal")
    st.write("Log trades here (coming soon)")

with tab5:
    st.subheader("Hermes AI Prompts")
    st.code("Copy the improved prompt from our conversation into Hermes", language="markdown")

st.sidebar.success("✅ Professional Quant Mode Active")
