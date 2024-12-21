import yfinance as yf
import pandas as pd

# Get list of tickers
SP500_tickers = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]['Symbol'].tolist()
tickers = ' '.join(SP500_tickers)
# Get data from yahoo finance library for all members
data = yf.download(tickers, period="1mo", actions=False, interval="1d").round(2)
data.to_csv("prices3")

# Select only the Close prices columns
prices3 = pd.read_csv("prices3")
closePrices = prices3.iloc[:, 504:1005]
closePrices.to_csv("closePrices")

# Reformat first column
dateCol = prices3.iloc[:, 0]
closePrices = pd.read_csv("closePrices")
closePrices.iloc[:, 0] = dateCol
closePrices.to_csv("closePrices")

Remove 1st and 3rd rows manually from the csv file
Calculate share price changes and calculate variance and covariances
closePrices = pd.read_csv("closePrices")
basePrices = closePrices.iloc[0]
priceChanges = (closePrices.iloc[:, 2:] - basePrices).round(5) # Calculate change in share price from 1st day
priceChanges.to_csv("priceChanges")
priceChanges.var().to_csv("stockVariance")
priceChanges.cov().to_csv("stockCovariance")

