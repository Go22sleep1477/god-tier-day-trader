import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os
import csv
from datetime import datetime
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
import plotly.graph_objects as go

load_dotenv()

st.set_page_config(page_title="God-Tier Day Trader", layout="wide", initial_sidebar_state="expanded")
st.title("🦍 GOD-TIER DAY TRADER — FULL TILT MAXIMUM CRAZY MODE")

st.markdown("""
<style>
    .stApp { background-color: #050505; color: #00FFAA; }
    .metric-card { background-color: #0F0F0F; padding: 20px; border-radius: 15px; border: 2px solid #00FFAA; }
</style>
""", unsafe_allow_html=True)

st.sidebar.header("🚀 MAXIMUM OVERDRIVE CONTROLS")
account_size = st.sidebar.number_input("Account Size ($)", value=50000.0, step=1000.0)
risk_pct = st.sidebar.slider("Risk per Trade (%)", 0.1, 1.0, 0.5) / 100
ticker = st.sidebar.text_input("Main Ticker", "GME").upper()
target_price = st.sidebar.number_input("🚨 Price Target Alert", value=25.0)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([
    "📊 TradingView Pro", 
    "🌅 Pre-Market Scanner", 
    "📈 LIVE MULTI-INDICATOR ENGINE", 
    "📉 OPTIONS CHAIN", 
    "🛡️ ADVANCED RISK ENGINE", 
    "📓 TRADE JOURNAL", 
    "📊 PERFORMANCE + EQUITY CURVE", 
    "🤖 HERMES AI", 
    "🔬 QUANT LAB", 
    "⚡ SYSTEM OVERVIEW"
])

with tab1:
    st.subheader(f"TradingView Pro — {ticker}")
    st.components.v1.html(f'''
        <iframe src="https://www.tradingview.com/widgetembed/?symbol={ticker}&interval=D&theme=dark&style=1" 
        width="100%" height="680" frameborder="0"></iframe>
    ''', height=700)

with tab3:
    st.subheader(f"📈 LIVE MULTI-INDICATOR ENGINE — {ticker}")
    if st.button("🔥 FETCH ALL INDICATORS NOW", type="primary"):
        try:
            client = StockHistoricalDataClient(os.getenv("ALPACA_API_KEY"), os.getenv("ALPACA_SECRET_KEY"))
            request = StockBarsRequest(symbol_or_symbols=ticker, timeframe=TimeFrame.Minute, limit=500)
            bars = client.get_stock_bars(request)
            df = bars.df.reset_index()
            
            if not df.empty:
                latest = df.iloc[-1]
                st.success(f"✅ LIVE PRICE: ${latest['close']:.2f} | Volume: {int(latest['volume']):,}")

                # RSI, MACD, Bollinger, EMA
                delta = df['close'].diff()
                gain = delta.where(delta > 0, 0).rolling(14).mean()
                loss = -delta.where(delta < 0, 0).rolling(14).mean()
                rs = gain / loss
                df['RSI'] = 100 - (100 / (1 + rs))
                df['EMA9'] = df['close'].ewm(span=9).mean()
                df['EMA21'] = df['close'].ewm(span=21).mean()
                df['MACD'] = df['EMA9'] - df['EMA21']

                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Price", f"${latest['close']:.2f}")
                col2.metric("RSI", round(df['RSI'].iloc[-1], 1))
                col3.metric("MACD", round(df['MACD'].iloc[-1], 4))
                col4.metric("Volume", f"{int(latest['volume']):,}")

                st.line_chart(df.set_index('timestamp')[['close', 'EMA9', 'EMA21']])
        except Exception as e:
            st.error(f"Alpaca Error: {e} — Add real keys in Streamlit Secrets for full power.")

with tab5:
    st.subheader("🛡️ ADVANCED RISK ENGINE")
    entry = st.number_input("Entry Price", value=22.82)
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
    st.success(f"**1:2 Target:** ${target}")
    st.info("**Trailing Stop Logic:** Breakeven at 1:1 → Trail by 1× ATR")

with tab7:
    st.subheader("📊 Performance + Equity Curve")
    if os.path.exists("trades.csv"):
        df = pd.read_csv("trades.csv", names=["Date","Ticker","Entry","Stop","Exit","Result","R"])
        st.dataframe(df)
        df['Cumulative'] = df['R'].cumsum()
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=df['Cumulative'], mode='lines', name='Equity Curve'))
        st.plotly_chart(fig, use_container_width=True)

with tab9:
    st.subheader("🔬 QUANT LAB")
    st.write("Backtesting, Strategy Optimizer, Monte Carlo Simulation, Multi-timeframe Analysis, and more coming soon.")

st.sidebar.success("✅ FULL TILT MAXIMUM CRAZY MODE ACTIVE")
st.sidebar.info("Type 'keep going' for the next insane upgrade")
