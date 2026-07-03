import streamlit as st
import pandas as pd

st.title("📉 Advanced Options Chain")
st.caption("Long & Short Calls / Puts • Realistic Data")

ticker = st.text_input("Ticker", "GME").upper()
st.subheader(f"Options Chain for {ticker} — Example Data (Live coming with full Alpaca)")

# Simulated realistic options data
calls = pd.DataFrame({
    "Strike": [20, 22, 23, 25, 28],
    "Long Call Premium": [3.45, 2.15, 1.65, 0.95, 0.45],
    "Short Call Premium": [3.40, 2.10, 1.60, 0.90, 0.40],
    "IV (%)": [68, 65, 62, 58, 55],
    "Volume": [12450, 8750, 15600, 9800, 4200],
    "Open Interest": [45200, 38900, 52100, 31200, 18500],
    "Delta": [0.78, 0.62, 0.55, 0.42, 0.28]
})

puts = pd.DataFrame({
    "Strike": [20, 22, 23, 25, 28],
    "Long Put Premium": [0.65, 1.25, 1.75, 2.85, 4.75],
    "Short Put Premium": [0.60, 1.20, 1.70, 2.80, 4.70],
    "IV (%)": [72, 68, 65, 61, 57],
    "Volume": [8900, 12400, 16700, 9800, 5400],
    "Open Interest": [31200, 45800, 62100, 28900, 15400],
    "Delta": [-0.22, -0.38, -0.45, -0.58, -0.72]
})

tab_c, tab_p = st.tabs(["📈 Call Options", "📉 Put Options"])

with tab_c:
    st.subheader("Call Options (Bullish Bias)")
    st.dataframe(calls, use_container_width=True, hide_index=True)
    
    st.write("**Strategy Ideas:**")
    st.write("- **Long Call**: Bullish directional bet (high delta)")
    st.write("- **Short Call**: Income / covered call strategy (collect premium)")

with tab_p:
    st.subheader("Put Options (Bearish / Protective Bias)")
    st.dataframe(puts, use_container_width=True, hide_index=True)
    
    st.write("**Strategy Ideas:**")
    st.write("- **Long Put**: Bearish bet or portfolio protection")
    st.write("- **Short Put**: Bullish / cash-secured put (collect premium)")

st.subheader("Quick Options Strategy Builder")
strategy = st.selectbox("Choose Strategy", [
    "Long Call (Bullish)", 
    "Short Call (Neutral/Bearish)", 
    "Long Put (Bearish)", 
    "Short Put (Bullish/Income)"
])

if strategy == "Long Call (Bullish)":
    st.success("Long Call: High upside, limited risk. Good for strong bullish conviction.")
elif strategy == "Short Call (Neutral/Bearish)":
    st.warning("Short Call: Collect premium. High risk if price surges. Best with covered stock.")
elif strategy == "Long Put (Bearish)":
    st.success("Long Put: Limited risk, high reward on downside moves.")
elif strategy == "Short Put (Bullish/Income)":
    st.info("Short Put: Bullish income strategy. Risk of owning stock if assigned.")

st.info("**Note:** Real options data + Greeks (Delta, Gamma, Theta, Vega) will be added once full Alpaca options access is enabled.")
