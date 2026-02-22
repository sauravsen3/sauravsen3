# 📊 Stock Price Analysis Dashboard

A simple web-based tool to analyse stock price trends using real market data, built with Python and Streamlit.

## About Me

I am a Mechatronics Engineering graduate and a postgraduate in Finance from Henley Business School, looking to enter the field of finance in data science, machine learning, or quantitative finance. This project is part of a series of quantitative finance projects I am building to demonstrate my interest and knowledge in the field.

- 💼 LinkedIn: [linkedin.com/in/sauravsen34](https://www.linkedin.com/in/sauravsen34)
- 📧 Email: saurav0sen34@gmail.com

---

## What Does This App Do?

This app gives a rough idea about stock price trends using key market indicators — volume, moving averages, and daily returns. Rather than just showing raw price, it layers in context that helps identify whether a stock is trending up or down, how volatile it is, and how actively it is being traded.

---

## What Can A User Do?

- Enter **any stock ticker** (e.g. AAPL, TSLA, BARC.L, LLOY.L)
- Set a **custom date range** to analyse any historical period
- Instantly see three key charts and a summary of key metrics

---

## Outputs

**Summary Metrics**
- Current price
- Total return over the selected period
- Latest trading volume

**Charts**

| Chart | What It Shows |
|-------|--------------|
| Price + Moving Averages | Closing price with 50-day and 200-day moving averages overlaid |
| Daily Returns | Bar chart of daily percentage returns — shows volatility and event-driven spikes |
| Trading Volume | Daily volume — helps identify whether price moves are backed by conviction |

---

## Key Concepts

**Moving Averages** — smooth out daily noise to reveal the underlying price trend. When price crosses above the 50-day MA it signals upward momentum. When the 50-day crosses above the 200-day it forms a Golden Cross — a widely watched bullish signal.

**Daily Returns** — percentage change in price each day. Large spikes indicate sensitivity to news, earnings, or market events. Long-term total return tells you where the stock ended up despite the noise.

**Volume** — the number of shares traded. A big price move on high volume is a strong signal. The same move on low volume is much weaker.

---

## Project Structure

```
stock-price-dashboard/
│
├── stock_dashboard.py    # All logic and Streamlit app
└── requirements.txt      # Python dependencies
```

---

## How To Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/sauravsen3/stock-price-dashboard.git
cd stock-price-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run stock_dashboard.py
```

---

## Tech Stack

- **Python** — core language
- **yfinance** — fetches real stock data from Yahoo Finance
- **pandas** — data manipulation and indicator calculation
- **matplotlib** — charting
- **streamlit** — interactive web interface
- **datetime** — handling custom date ranges

---

*Part of a series of quantitative finance projects. Previous: Options Pricing Engine. Next: Financial Data Pipeline.*
