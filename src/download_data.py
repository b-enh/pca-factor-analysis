import yfinance as yf
import pandas as pd
import os

os.makedirs("../dara/raw", exist_ok=True)

tickers = ["AAPL", "MSFT", "GOOG"]
data = yf.download(tickers, start="2021-01-01", end="2025-01-01")

data.to_csv("../data/raw/test_3stocks.csv")
print("Raw data saved")