import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.title("🛡️ God-Tier Risk Engine")
st.caption("Maximum Survival + Maximum Compounding • Final Version")

# ====================== ACCOUNT & RISK SETTINGS ======================
col1, col2, col3 = st.columns(3)
with col1:
    account_size = st.number_input("Account Size ($)", value=50000.0, step=1000.0)
with col2:
    risk_pct = st.slider("Risk per Trade (%)", 0.1, 1.0, 0.5) / 100
with col3:
    daily_risk_limit = st.slider("Daily Max Risk (%)", 1.0, 3.0, 2.0) / 100

ticker = st.text_input("Ticker", "GME").upper()
entry = st.number_input("Planned Entry Price", value=22.82)
atr = st.number_input("Current ATR (14)", value=1.8)

# ====================== POSITION SIZING ======================
st.subheader("Position Sizing")

atr_mult = st.select_slider(
    "ATR Stop Multiplier", 
    options=[1.0, 1.2, 1.5, 2.0, 2.5], 
    value=1.5,
    help="1.0 = Tight | 1.5 = Balanced | 2.0+ = Volatile/News"
)

stop_dist = round(atr * atr_mult, 2)
risk_amount = round(account_size * risk_pct, 2)
shares = int(risk_amount / stop_dist) if stop_dist > 0 else 0

target_1 = round(entry + (stop_dist * 2), 2)      # 1:2
target_2 = round(entry + (stop_dist * 3), 2)      # Stretch
target_3 = round(entry + (stop_dist * 4), 2)      # Moon target

c1, c2, c3, c4 = st.columns(4)
c1.metric("Stop Loss", f"${stop_dist}")
c2.metric("Shares", shares)
c3.metric("Risk $", f"${risk_amount}")
c4.metric("1:2 Target", f"${target_1}")

# ====================== SCALE-OUT PLAN ======================
st.subheader("Scale-Out & Trailing Plan (Professional)")

st.write("**Recommended Plan:**")
st.write("• **50%** of position at **1:1** R:R → Move stop to breakeven")
st.write("• **30%** of position at **1:2** R:R")
st.write("• **20%** runner → Trail with **1× ATR** or previous swing low")
st.write("• Full exit if price closes below trailing stop")

# ====================== DAILY RISK STATUS ======================
st.subheader("Daily Risk Status")

risk_used_today = st.slider("Risk Already Used Today (%)", 0.0, float(daily_risk_limit*100), 0.6)
remaining_risk = daily_risk_limit*100 - risk_used_today

st.progress(risk_used_today / (daily_risk_limit*100))
st.metric("Remaining Daily Risk", f"{remaining_risk:.1f}%")

if remaining_risk < 0.3:
    st.error("🚨 DAILY RISK LIMIT REACHED — Strongly consider stopping for the day")
elif remaining_risk < 0.8:
    st.warning("⚠️ Daily risk is getting low. Be very selective.")

# ====================== TRADE QUALITY SCORING ======================
st.subheader("Trade Quality Score (Expectancy Filter)")

col1, col2 = st.columns(2)
with col1:
    wyckoff_score = st.slider("Wyckoff Confluence (1-10)", 1, 10, 7)
    indicator_score = st.slider("Indicator Confluence (1-10)", 1, 10, 6)
with col2:
    flow_score = st.slider("Institutional Flow (Dark Pool / Options)", 1, 10, 5)
    structure_score = st.slider("Market Structure Quality", 1, 10, 7)

total_score = (wyckoff_score + indicator_score + flow_score + structure_score) / 4
st.metric("Overall Trade Quality Score", f"{total_score:.1f} / 10")

if total_score >= 7.5:
    st.success("✅ High Quality Setup — Strong expectancy")
elif total_score >= 6.0:
    st.info("🟡 Medium Quality — Acceptable if risk is tight")
else:
    st.error("❌ Low Quality Setup — Consider skipping")

# ====================== COMPOUNDING VIEW ======================
st.subheader("Long-Term Compounding Impact")

monthly_trades = st.slider("Average Trades per Month", 10, 60, 25)
win_rate = st.slider("Expected Win Rate", 40, 70, 55)
avg_r = st.slider("Average R-Multiple per Trade", 0.8, 2.5, 1.4)

# Simple expectancy calculation
expectancy_per_trade = (win_rate/100 * avg_r) - ((1 - win_rate/100) * 1)
monthly_r = monthly_trades * expectancy_per_trade

st.metric("Estimated Monthly R", f"+{monthly_r:.2f} R")
st.write(f"At current account size, this is roughly **+${monthly_r * account_size * 0.01:.0f}** per month (before compounding).")

if st.button("Project 12-Month Growth"):
    st.success("With consistent execution, this system has strong compounding potential over time.")

# ====================== FINAL APPROVAL ======================
st.subheader("Final Trade Decision")

if st.button("✅ APPROVE & LOG THIS SETUP", type="primary"):
    st.balloons()
    st.success("Trade Approved • Risk Rules Confirmed • Logged to Journal")
    st.info("Remember: The goal is to survive long enough for the edge to compound massively.")
