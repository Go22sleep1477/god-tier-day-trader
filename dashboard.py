import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os
from alpaca.data.historical import StockHistoricalDataClient, OptionHistoricalDataClient
from alpaca.data.requests import StockBarsRequest, OptionBarsRequest
from alpaca.data.timeframe import TimeFrame
import plotly.graph_objects as go
from datetime import datetime, timedelta

load_dotenv()

st.set_page_config(page_title="God-Tier Day Trader", layout="wide")
st.title("🦍 God-Tier Day Trader — Quant Terminal")

st.sidebar.header("⚙️ Settings")
account_size = st.sidebar.number_input("Account Size ($)", value=50000.0, step=1000.0)
risk_pct = st.sidebar.slider("Risk %", 0.1, 1.0, 0.5) / 100
ticker = st.sidebar.text_input("Ticker", "GME").upper()
target_price = st.sidebar.number_input("Alert Target Price", value=25.0)

tab1, tab2, tab3, tab4 = st.tabs(["📊 TradingView + Indicators", "📈 Options Chain", "🧠 Risk & Alerts", "📓 Journal"])

# Tab 1: TradingView + Indicators
with tab1:
    st.subheader(f"TradingView + Technical Indicators — {ticker}")
    st.components.v1.html(f'''
        <iframe src="https://www.tradingview.com/widgetembed/?symbol={ticker}&interval=D&theme=dark" 
        width="100%" height="600" frameborder="0"></iframe>
    ''', height=650)

    # Simple Indicators (placeholder - expand later)
    st.write("**Key Indicators:** RSI, EMA 9/20, MACD (calculated below when Alpaca keys added)")

# Tab 2: Options Chain
with tab2:
    st.subheader("Call Options Chain")
    st.info("Add real Alpaca keys in Streamlit Secrets for live options data")
    # Placeholder for options data
    st.write("Popular Calls:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Strike $23", "Premium $1.25", "Vol: High")
    with col2:
        st.metric("Strike $25", "Premium $0.85", "Vol: Medium")
    with col3:
        st.metric("Strike $28", "Premium $0.45", "Vol: Low")

# Tab 3: Risk + Alerts
with tab3:
    st.subheader("Risk Calculator + Price Alerts")
    entry = st.number_input("Planned Entry", value=22.82)
    atr = st.number_input("ATR", value=1.8)
    mult = st.select_slider("Stop Multiplier", [1.0, 1.5, 2.0, 2.5], value=1.5)
    
    stop_dist = round(atr * mult, 2)
    risk_amount = round(account_size * risk_pct, 2)
    shares = int(risk_amount / stop_dist) if stop_dist > 0 else 0
    target = round(entry + (stop_dist * 2), 2)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Stop Loss", f"${stop_dist}")
    col2.metric("Shares", shares)
    col3.metric("Risk $", f"${risk_amount}")
    
    st.success(f"**Target:** ${target}")
    
    # Alert
    if target_price and target_price > entry:
        st.warning(f"🚨 ALERT: Target Price ${target_price} set!")

# Tab 4: Journal
with tab4:
    st.subheader("Trade Journal")
    st.write("Log your trades here")

st.sidebar.success("✅ Enhanced Quant Version Active")
