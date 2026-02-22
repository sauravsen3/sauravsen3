import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# 1. Page config and title
st.set_page_config(page_title="Stock Price Dashboard", page_icon="📊")
st.title("📊 Stock Price Analysis Dashboard")
st.sidebar.header("⚙️ Settings")

# 2. Sidebar inputs (define ticker and dates FIRST)
ticker = st.sidebar.text_input("Enter Stock Ticker", value="AAPL")
start_date = st.sidebar.date_input("Start Date", datetime.now() - timedelta(days=365*2))
end_date = st.sidebar.date_input("End Date", datetime.now())

# 3. Fetch data (now ticker and dates exist)
data = yf.download(ticker, start=start_date, end=end_date)

if data.empty:
    st.error("No data found. Please check the ticker symbol and try again.")
    st.stop()

# 4. Calculate indicators (now data exists)
data['Daily_Return'] = data['Close'].pct_change()
data['MA50'] = data['Close'].rolling(window=50).mean()
data['MA200'] = data['Close'].rolling(window=200).mean()

# 5. Summary metrics
st.subheader(f"{ticker} — Summary")
col1, col2, col3 = st.columns(3)

current_price = data['Close'].iloc[-1]
start_price = data['Close'].iloc[0]
total_return = ((current_price - start_price) / start_price) * 100
current_volume = data['Volume'].iloc[-1]

col1.metric("Current Price", f"${current_price:.2f}")
col2.metric("Total Return", f"{total_return:.2f}%")
col3.metric("Volume (Latest)", f"{current_volume:,.0f}")

# 6. Price chart with moving averages
st.subheader("📈 Price Chart with Moving Averages")
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(data.index, data['Close'], color="blue", label="Close Price")
ax.plot(data.index, data['MA50'], color="red", label="50-Day MA")
ax.plot(data.index, data['MA200'], color="green", label="200-Day MA")
ax.set_xlabel("Date")
ax.set_ylabel("Price ($)")
ax.legend()
st.pyplot(fig)

# 7. Daily returns chart
st.subheader("📊 Daily Returns")
fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(data.index, data['Daily_Return'], color="green", label="Daily Return")
ax.set_xlabel("Date")
ax.set_ylabel("Daily Return (%)")
ax.legend()
st.pyplot(fig)

# 8. Volume chart
st.subheader("📊 Trading Volume")
fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(data.index, data['Volume'], color="blue", label="Volume")
ax.set_xlabel("Date")
ax.set_ylabel("Volume")
ax.legend()
st.pyplot(fig)
