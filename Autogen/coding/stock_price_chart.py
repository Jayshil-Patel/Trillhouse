# filename: stock_price_chart.py
import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock tickers
tickers = ["NVDA", "TSLA"]

# Download the stock data
data = yf.download(tickers, start="2021-01-01", end="2021-12-31")

# Calculate the price change YTD
data["Price Change YTD"] = (data["Adj Close"].div(data["Adj Close"].iloc[0]).sub(1)).mul(100)

# Plot the chart
plt.figure(figsize=(10, 6))
for ticker in tickers:
    plt.plot(data.index, data["Price Change YTD"][ticker], label=ticker)

plt.title("Stock Price Change YTD")
plt.xlabel("Date")
plt.ylabel("Price Change (%)")
plt.legend()
plt.grid(True)
plt.show()