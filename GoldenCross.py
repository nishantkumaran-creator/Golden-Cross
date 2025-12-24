import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Definining the stock symbol and time period
ticker1 = "NVDA"
ticker2 = "GOOGL"
start_date = "2020-01-01"
end_date = "2024-01-01"

#downloading the data
data1 = yf.download(ticker1, start=start_date, end=end_date)
data2 = yf.download(ticker2, start=start_date, end=end_date)

#Caluculate the moving averages
data1["SMA_50"] = data1['Close'].rolling(window=50).mean()
data1["SMA_200"] = data1['Close'].rolling(window=200).mean()
data2["SMA_50"] = data2['Close'].rolling(window=50).mean()
data2["SMA_200"] = data2['Close'].rolling(window=200).mean()

#Create 2 separate plots(subplots) for each stock
fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize=(16, 12), sharex=True)

# Plotting the closing prices and moving averages
# Plot Ticker 1 on the top chart (ax1)
ax1.plot(data1['Close'], label=f'{ticker1} Price', alpha=0.5, color='gray')
ax1.plot(data1["SMA_50"], label='SMA 50', color='orange')
ax1.plot(data1["SMA_200"], label='SMA 200', color='red')
ax1.set_title(f'{ticker1} Analysis')
ax1.legend()

# Plot Ticker 2 on the bottom chart (ax2)
ax2.plot(data2['Close'], label=f'{ticker2} Price', alpha=0.5, color='gray')
ax2.plot(data2["SMA_50"], label='SMA 50', color='cyan')
ax2.plot(data2["SMA_200"], label='SMA 200', color='blue')
ax2.set_title(f'{ticker2} Analysis')
ax2.legend()

# Adjusts spacing so titles don't overlap
plt.tight_layout() 
plt.show()