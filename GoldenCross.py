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

# Plotting the closing prices and moving averages
plt.figure(figsize=(16, 8))
plt.plot(data1['Close'], label=f'{ticker1} Close Price', alpha = 0.5)
plt.plot(data1["SMA_50"], label=f'{ticker1} 50-Day SMA', color='orange')
plt.plot(data1["SMA_200"], label=f'{ticker1} 200-Day SMA', color='red')
plt.plot(data2['Close'], label=f'{ticker2} Close Price', alpha = 0.5)
plt.plot(data2["SMA_50"], label=f'{ticker2} 50-Day SMA', color='blue')
plt.plot(data2["SMA_200"], label=f'{ticker2} 200-Day SMA', color='darkblue')

plt.title(f'{ticker1} and {ticker2} Simple Moving Average Crossover')
plt.legend()
plt.show()