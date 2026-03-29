import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# 下载数据
symbol = 'AAPL'  # 选择的股票，例如苹果公司
start_date = '2020-01-01'
end_date = '2023-01-01'

data = yf.download(symbol, start=start_date, end=end_date)

# 计算移动平均线
short_window = 20
long_window = 50

data['Short_MA'] = data['Close'].rolling(window=short_window).mean()
data['Long_MA'] = data['Close'].rolling(window=long_window).mean()

# 检查移动平均线
print(data[['Close', 'Short_MA', 'Long_MA']].dropna())

# 生成信号
data['Signal'] = 0
data['Signal'][short_window:] = np.where(data['Short_MA'][short_window:] > data['Long_MA'][short_window:], 1, 0)
data['Position'] = data['Signal'].diff()

# 检查生成的信号
print(data[['Close', 'Short_MA', 'Long_MA', 'Signal', 'Position']].dropna())

# 可视化
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', alpha=0.5)
plt.plot(data['Short_MA'], label='20-Day MA', alpha=0.75)
plt.plot(data['Long_MA'], label='50-Day MA', alpha=0.75)

# 标记买入信号
plt.plot(data[data['Position'] == 1].index,
         data['Close'][data['Position'] == 1],
         '^', markersize=10, color='g', label='Buy Signal')

# 标记卖出信号
plt.plot(data[data['Position'] == -1].index,
         data['Close'][data['Position'] == -1],
         'v', markersize=10, color='r', label='Sell Signal')

plt.title(f'{symbol} Moving Average Crossover Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()
