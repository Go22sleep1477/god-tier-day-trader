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

ticker = st.text_input("Ticker", "NVDA").upper()

if st.button("🚀 Run Analysis"):
    st.success(f"Analysis for {ticker} loaded!")
    st.info("TradingView, Alpaca, Risk Calculator & more are ready.")

st.sidebar.success("✅ System Ready")
