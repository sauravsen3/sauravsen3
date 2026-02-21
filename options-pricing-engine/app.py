import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from black_scholes import black_scholes_price
from greeks import all_greeks
from monte_carlo import monte_carlo_price

st.set_page_config(page_title="Options Pricing Engine", page_icon="📈")
st.title("📈 Options Pricing Engine")
st.sidebar.header("🔧 Option Parameters")

S = st.sidebar.number_input("Stock Price (S) £", min_value=1.0, max_value=10000.0, value=100.0)
K = st.sidebar.number_input("Strike Price (K) £", min_value=1.0, max_value=10000.0, value=100.0)
T_days = st.sidebar.slider("Time to Expiry (days)", min_value=1, max_value=730, value=90)
r_pct = st.sidebar.slider("Risk-Free Rate (%)", min_value=0.0, max_value=15.0, value=5.0)
sigma_pct = st.sidebar.slider("Volatility (%)", min_value=1.0, max_value=150.0, value=20.0)
option_type = st.sidebar.radio("Option Type", options=["call", "put"])

# Convert to decimals for the functions
T = T_days / 365
r = r_pct / 100
sigma = sigma_pct / 100

bs_price = black_scholes_price(S, K, T, r, sigma, option_type)
mc_result = monte_carlo_price(S, K, T, r, sigma, option_type)
greeks = all_greeks(S, K, T, r, sigma, option_type)

st.subheader("💰 Option Price")
col1, col2 = st.columns(2)
col1.metric("Black-Scholes Price", f"£{bs_price}")
col2.metric("Monte Carlo Price", f"£{mc_result['price']}")

st.subheader("🧮 The Greeks")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Delta Δ", greeks["Delta"])
col2.metric("Gamma Γ", greeks["Gamma"])
col3.metric("Vega ν",  greeks["Vega"])
col4.metric("Theta Θ", greeks["Theta"])
col5.metric("Rho ρ",   greeks["Rho"])

spot_range = np.linspace(S * 0.5, S * 1.5, 200)
prices = [black_scholes_price(s, K, T, r, sigma, option_type) for s in spot_range]

st.subheader("📉 Option Price vs Stock Price")
fig, ax = plt.subplots()
ax.plot(spot_range, prices)
ax.axvline(S, color="red", linestyle="--", label=f"Current Price £{S}")
ax.axvline(K, color="green", linestyle="--", label=f"Strike £{K}")
ax.set_xlabel("Stock Price £")
ax.set_ylabel("Option Price £")
ax.legend()
st.pyplot(fig)
