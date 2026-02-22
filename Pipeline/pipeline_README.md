# 🔧 Financial Data Pipeline

A Python pipeline that automatically fetches, cleans, enriches, and saves stock market data from Yahoo Finance. Built as reusable infrastructure for downstream quantitative finance projects.

## About Me

I am a Mechatronics Engineering graduate and a postgraduate in Finance from Henley Business School, looking to enter the field of finance in data science, machine learning, or quantitative finance.

- 💼 LinkedIn: [linkedin.com/in/sauravsen34](https://www.linkedin.com/in/sauravsen34)
- 📧 Email: saurav0sen34@gmail.com

---

## What Does This Pipeline Do?

In real finance firms, every quant model and risk system depends on clean, reliable data flowing in continuously. A broken or dirty data feed means wrong prices, wrong signals, and wrong decisions.

This pipeline simulates that infrastructure — it fetches raw stock data, cleans it, enriches it with calculated indicators, and saves it as a CSV file ready for any downstream project to use.

---

## The Four Steps

```
fetch_data() → clean_data() → enrich_data() → save_data()
```

**1. fetch_data()** — downloads OHLCV data from Yahoo Finance for any ticker and date range. Handles missing tickers gracefully.

**2. clean_data()** — removes rows with missing Close prices, removes duplicate dates, and sorts chronologically oldest to newest.

**3. enrich_data()** — adds four calculated columns:
- `Daily_Return` — percentage change in price each day
- `MA50` — 50-day moving average
- `MA200` — 200-day moving average
- `Volatility_20d` — 20-day rolling standard deviation of returns

**4. save_data()** — saves the enriched DataFrame to a timestamped CSV file in a local `data/` folder.

---

## Why A Pipeline?

Without a pipeline, every project fetches and cleans data independently — duplicating work and risking inconsistency. With a pipeline, data is fetched once, cleaned once, and reused everywhere. This is how production systems in banks and funds are built.

A natural next step would be scheduling this pipeline to run automatically at market close every weekday using a cron job on a Linux server — making it a live, automated data feed.

---

## How To Run

```bash
# 1. Clone the repository
git clone https://github.com/sauravsen3/financial-data-pipeline.git
cd financial-data-pipeline

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the pipeline
python pipeline.py
```

Output:
```
--- Running pipeline for AAPL ---
Fetched 504 rows for AAPL
Clean data: 504 rows remaining
Enriched data with 9 columns
Data saved to data/AAPL_20260222.csv
--- Pipeline complete ---
```

A `data/` folder is created automatically containing a timestamped CSV for each ticker.

---

## Project Structure

```
financial-data-pipeline/
│
├── pipeline.py         # Full pipeline — fetch, clean, enrich, save
├── requirements.txt    # Python dependencies
└── data/               # Output folder (auto-created)
    ├── AAPL_20260222.csv
    ├── MSFT_20260222.csv
    └── BARC.L_20260222.csv
```

---

## Tech Stack

- **yfinance** — fetches real market data from Yahoo Finance
- **pandas** — data cleaning, manipulation, CSV export
- **numpy** — numerical operations
- **os** — file system management, cross-platform path handling

---

*Part of a series of quantitative finance projects. Previous: Stock Price Dashboard. Next: Predicting Stock Returns with ML.*
