import streamlit as st

st.title("🛡️ Advanced Risk Engine")
st.caption("Capital Preservation + Compounding • Professional Grade")

col1, col2, col3 = st.columns(3)
with col1:
    account_size = st.number_input("Account Size ($)", value=50000.0, step=1000.0)
with col2:
    risk_pct = st.slider("Risk per Trade (%)", 0.1, 1.0, 0.5) / 100
with col3:
    daily_limit = st.slider("Daily Max Risk (%)", 1.0, 3.0, 2.0) / 100

ticker = st.text_input("Ticker", "GME").upper()
entry = st.number_input("Planned Entry", value=22.82)
atr = st.number_input("Current ATR", value=1.8)
atr_mult = st.select_slider("ATR Multiplier", [1.0, 1.2, 1.5, 2.0, 2.5], value=1.5)

stop_dist = round(atr * atr_mult, 2)
risk_amount = round(account_size * risk_pct, 2)
shares = int(risk_amount / stop_dist) if stop_dist > 0 else 0
target1 = round(entry + stop_dist * 2, 2)
target2 = round(entry + stop_dist * 3, 2)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Stop Distance", f"${stop_dist}")
c2.metric("Shares", shares)
c3.metric("Risk $", f"${risk_amount}")
c4.metric("1:2 Target", f"${target1}")

st.success("**Scale-Out Plan:** 50% at 1:1 → Breakeven → Trail remainder with 1× ATR")

st.subheader("Daily Risk Status")
risk_used = st.slider("Risk Used Today (%)", 0.0, float(daily_limit*100), 0.8)
st.progress(risk_used / (daily_limit*100))
st.metric("Remaining Daily Risk", f"{daily_limit*100 - risk_used:.1f}%")

if st.button("✅ Approve Trade Setup", type="primary"):
    st.balloons()
    st.success("Trade Approved • Risk Rules Confirmed")
