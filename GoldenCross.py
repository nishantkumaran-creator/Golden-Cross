import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # <--- NEW IMPORT

def analyze_stock(ticker):
    ticker = ticker.upper().strip()
    start_date = "2020-01-01"
    end_date = "2024-01-01"

    print(f"Downloading data for {ticker}...")
    data = yf.download(ticker, start=start_date, end=end_date, progress=False)

    if data.empty:
        print(f"Error: Could not find data for symbol '{ticker}'.")
        return

    # 1. Calculate Moving Averages
    data["SMA_50"] = data['Close'].rolling(window=50).mean()
    data["SMA_200"] = data['Close'].rolling(window=200).mean()
    
    # --- NEW QUANT LOGIC STARTS HERE ---

    # 2. Generate Signals (1 = Buy, 0 = Sell)
    # np.where(condition, value_if_true, value_if_false)
    data['Signal'] = np.where(data['SMA_50'] > data['SMA_200'], 1, 0)

    # 3. Calculate Daily Returns
    # pct_change() gives the daily % movement of the stock
    data['Stock_Return'] = data['Close'].pct_change()

    # 4. Calculate Strategy Returns
    # We use .shift(1) because we trade the NEXT day based on today's signal
    data['Strategy_Return'] = data['Signal'].shift(1) * data['Stock_Return']

    # 5. Calculate Cumulative Returns (Growth of $1)
    # cumprod() stands for cumulative product
    data['Cumulative_Market'] = (1 + data['Stock_Return']).cumprod()
    data['Cumulative_Strategy'] = (1 + data['Strategy_Return']).cumprod()

    # --- PLOTTING UPDATE ---
    
    # We now create TWO plots: One for price, one for performance
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

    # Plot 1: The Price & moving averages (Visual Check)
    ax1.plot(data['Close'], label=f'{ticker} Price', alpha=0.5, color='gray')
    ax1.plot(data["SMA_50"], label='SMA 50', color='orange')
    ax1.plot(data["SMA_200"], label='SMA 200', color='red')
    ax1.set_title(f'{ticker} Price Analysis')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Plot 2: The Backtest (Performance Check)
    ax2.plot(data['Cumulative_Market'], label='Buy & Hold', color='gray', linestyle='--')
    ax2.plot(data['Cumulative_Strategy'], label='Golden Cross Strategy', color='green')
    ax2.set_title(f'{ticker} Strategy Performance (Growth of $1)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    # Optional: Print final result
    latest_strategy = data['Cumulative_Strategy'].iloc[-1]
    latest_market = data['Cumulative_Market'].iloc[-1]
    
    print(f"--- Results for {ticker} ---")
    print(f"Buy & Hold Return: {(latest_market - 1)*100:.2f}%")
    print(f"Strategy Return:   {(latest_strategy - 1)*100:.2f}%")
    print("-------------------------------")

# --- Main Block remains the same ---
if __name__ == "__main__":
    while True:
        user_input = input("\nEnter a stock ticker (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        analyze_stock(user_input)