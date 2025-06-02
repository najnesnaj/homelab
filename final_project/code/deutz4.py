import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Step 1: Download 20 years of DEZ.DE stock data
ticker = "DEZ.DE"
stock = yf.Ticker(ticker)
end_date = datetime.now()
start_date = end_date - timedelta(days=20*365)  # 20 years
df = stock.history(start=start_date, end=end_date)

# Step 2: Prepare data
prices = df['Close']  # Use closing prices
dates = df.index

# Step 3: Detect crossings at 3.8 and 5.7 euros
# Shift prices to compare with previous day for crossings
price_diff = prices.shift(1)  # Previous day's prices
buy_crossings = (prices <= 3.8) & (price_diff > 3.8) | (prices >= 3.8) & (price_diff < 3.8)
sell_crossings = (prices >= 5.7) & (price_diff < 5.7) | (prices <= 5.7) & (price_diff > 5.7)

# Step 4: Create the plot
plt.figure(figsize=(12, 6))
plt.plot(dates, prices, color='blue', label='DEZ.DE Share Price', linewidth=1.5)

# Step 5: Add colored background regions
# Light green background for prices between 0 and 3.8 euros
plt.axhspan(ymin=0, ymax=3.8, facecolor='lightgreen', alpha=0.3, label='Price < 3.8 EUR')
# Light red background for prices between 5.7 and 8 euros
plt.axhspan(ymin=5.7, ymax=8, facecolor='lightcoral', alpha=0.3, label='Price 5.7–8 EUR')

# Step 6: Add buy and sell markers
plt.scatter(dates[buy_crossings], prices[buy_crossings], color='green', marker='^', s=100, label='Buy (Cross 3.8 EUR)')
plt.scatter(dates[sell_crossings], prices[sell_crossings], color='red', marker='v', s=100, label='Sell (Cross 5.7 EUR)')

# Step 7: Add threshold lines for reference
plt.axhline(y=3.8, color='green', linestyle='--', alpha=0.5, label='3.8 EUR Threshold')
plt.axhline(y=5.7, color='red', linestyle='--', alpha=0.5, label='5.7 EUR Threshold')

# Step 8: Customize the plot
plt.title('DEUTZ Aktiengesellschaft (DEZ.DE) Share Price Over 20 Years')
plt.xlabel('Date')
plt.ylabel('Share Price (EUR)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Step 9: Save and display the plot
plt.savefig('dez_de_share_price_20years_background_markers.png')
plt.show()
