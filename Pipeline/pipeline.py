import yfinance as yf
import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)


def fetch_data(ticker, start_date, end_date):
    """
    Download stock data from Yahoo Finance.

    Returns:
        DataFrame — raw OHLCV data
    """
    data = yf.download(ticker, start=start_date, end=end_date)

    if data.empty:
        print(f"No data found for {ticker}")
        return None

    print(f"Fetched {len(data)} rows for {ticker}")
    return data


def clean_data(data):
    """
    Clean raw stock data — remove nulls, duplicates, sort by date.

    Returns:
        DataFrame — cleaned data
    """
    data = data.dropna(subset=['Close'])
    data = data[~data.index.duplicated()]
    data = data.sort_index()
    print(f"Clean data: {len(data)} rows remaining")
    return data


def enrich_data(data):
    """
    Add calculated columns to cleaned data.

    Returns:
        DataFrame — enriched data with indicators
    """
    data['Daily_Return'] = data['Close'].pct_change()
    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['MA200'] = data['Close'].rolling(window=200).mean()
    data['Volatility_20d'] = data['Daily_Return'].rolling(window=20).std()
    print(f"Enriched data with {len(data.columns)} columns")
    return data


def save_data(data, ticker):
    """
    Save enriched data to a CSV file.

    Returns:
        str — filepath where data was saved
    """
    filename = f"{ticker}_{datetime.now().strftime('%Y%m%d')}.csv"
    filepath = os.path.join("data", filename)
    data.to_csv(filepath)
    print(f"Data saved to {filepath}")
    return filepath


def run_pipeline(ticker, start_date, end_date):
    """
    Run the full pipeline: fetch → clean → enrich → save
    """
    print(f"\n--- Running pipeline for {ticker} ---")

    data = fetch_data(ticker, start_date, end_date)
    if data is None:
        return None

    data = clean_data(data)
    data = enrich_data(data)
    filepath = save_data(data, ticker)

    print(f"--- Pipeline complete ---\n")
    return data, filepath


# Run it
if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "BARC.L"]
    start = datetime.now() - timedelta(days=365*2)
    end = datetime.now()

    for ticker in tickers:
        run_pipeline(ticker, start, end)
