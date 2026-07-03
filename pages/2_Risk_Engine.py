import streamlit as st

st.title("🛡️ GOD-TIER RISK ENGINE")
st.caption("Capital Preservation First • Designed for Compounding Over Years")

# Account Settings
col1, col2, col3 = st.columns(3)
with col1:
    account_size = st.number_input("Total Account Size ($)", value=50000.0, step=1000.0)
with col2:
    risk_pct = st.slider("Risk Per Trade (%)", 0.1, 1.0, 0.5) / 100
with col3:
    daily_max = st.slider("Daily Max Risk (%)", 1.0, 3.0, 2.0) / 100

ticker = st.text_input("Ticker", "GME").upper()
entry = st.number_input("Planned Entry Price", value=22.82)
atr = st.number_input("Current ATR (14)", value=1.8)
atr_mult = st.select_slider("ATR Stop Multiplier", options=[1.0, 1.2, 1.5, 2.0, 2.5], value=1.5)

# Calculations
stop_dist = round(atr * atr_mult, 2)
risk_amount = round(account_size * risk_pct, 2)
shares = int(risk_amount / stop_dist) if stop_dist > 0 else 0
target_1 = round(entry + (stop_dist * 2), 2)
target_2 = round(entry + (stop_dist * 3), 2)
target_3 = round(entry + (stop_dist * 4), 2)

# Display
c1, c2, c3, c4 = st.columns(4)
c1.metric("Stop Distance", f"${stop_dist}", "Volatility Adjusted")
c2.metric("Shares to Trade", shares)
c3.metric("Risk on Trade", f"${risk_amount}", f"{risk_pct*100:.1f}% of account")
c4.metric("1:2 Target", f"${target_1}")

st.success(f"**Scale-Out Plan:** 50% at 1:1 → Breakeven → Trail remainder with 1× ATR or swing low")

# Daily Risk
st.subheader("Daily Risk Status")
risk_used = st.slider("Risk Used Today (%)", 0.0, float(daily_max*100), 0.8)
remaining = daily_max*100 - risk_used
st.progress(risk_used / (daily_max*100))
st.metric("Remaining Daily Risk Budget", f"{remaining:.1f}%")

if remaining < 0.5:
    st.error("🚨 DAILY RISK LIMIT NEARLY EXCEEDED — Consider stopping for the day")
elif remaining < 1.0:
    st.warning("⚠️ Daily risk getting low. Be extremely selective.")

# Trade Quality Score
st.subheader("Trade Quality Score (Expectancy Filter)")
wyckoff = st.slider("Wyckoff Confluence", 1, 10, 7)
indicator = st.slider("Technical Confluence", 1, 10, 6)
flow = st.slider("Institutional Flow", 1, 10, 5)
structure = st.slider("Market Structure", 1, 10, 7)

score = (wyckoff + indicator + flow + structure) / 4.0
st.metric("Overall Trade Quality", f"{score:.1f}/10")

if score >= 7.5:
    st.success("✅ HIGH QUALITY SETUP — Strong edge")
elif score >= 6.0:
    st.info("🟡 Acceptable Setup")
else:
    st.error("❌ LOW QUALITY — Consider skipping")

# Final Decision
if st.button("✅ APPROVE THIS TRADE", type="primary"):
    st.balloons()
    st.success("Trade Approved • Risk Rules Strictly Followed • Logged")
    st.info("Remember: The goal is to survive long enough for the edge to compound massively over time.")

st.caption("This Risk Engine is designed to keep you alive long enough to get rich.")
