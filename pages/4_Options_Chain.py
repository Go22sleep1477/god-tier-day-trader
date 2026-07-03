import streamlit as st
import pandas as pd

st.title("📉 Professional Options Chain")
st.caption("Long / Short • Calls & Puts")

ticker = st.text_input("Ticker", "GME").upper()

calls = pd.DataFrame({
    "Strike": [20, 22, 23, 25, 28],
    "Long Call Premium": [3.45, 2.15, 1.65, 0.95, 0.45],
    "Short Call Premium": [3.40, 2.10, 1.60, 0.90, 0.40],
    "IV (%)": [68, 65, 62, 58, 55],
    "Delta": [0.78, 0.62, 0.55, 0.42, 0.28]
})

puts = pd.DataFrame({
    "Strike": [20, 22, 23, 25, 28],
    "Long Put Premium": [0.65, 1.25, 1.75, 2.85, 4.75],
    "Short Put Premium": [0.60, 1.20, 1.70, 2.80, 4.70],
    "IV (%)": [72, 68, 65, 61, 57],
    "Delta": [-0.22, -0.38, -0.45, -0.58, -0.72]
})

tab_c, tab_p = st.tabs(["Call Options", "Put Options"])

with tab_c:
    st.dataframe(calls, use_container_width=True)

with tab_p:
    st.dataframe(puts, use_container_width=True)
