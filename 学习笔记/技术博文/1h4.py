import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# 获取历史数据
def get_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

# 计算 RSI
def compute_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()

    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data

# 生成交易信号
def generate_signals(data, rsi_overbought=70, rsi_oversold=30):
    data['Signal'] = 0
    data['Signal'][data['RSI'] < rsi_oversold] = 1  # 超卖，买入信号
    data['Signal'][data['RSI'] > rsi_overbought] = -1  # 超买，卖出信号
    data['Position'] = data['Signal'].diff()
    return data

# 绘制结果
def plot_results(data):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price', alpha=0.5)

    # 买入信号
    buy_signals = data[data['Position'] == 1]
    sell_signals = data[data['Position'] == -1]

    plt.plot(buy_signals.index,
             buy_signals['Close'],
             '^', markersize=10, color='g', label='Buy Signal')

    plt.plot(sell_signals.index,
             sell_signals['Close'],
             'v', markersize=10, color='r', label='Sell Signal')

    plt.title('RSI Trading Strategy')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()

# 主程序
if __name__ == "__main__":
    symbol = 'AAPL'  # 股票代码
    start_date = '2020-01-01'
    end_date = '2023-01-01'

    # 获取数据
    data = get_data(symbol, start_date, end_date)

    # 计算 RSI
    data = compute_rsi(data)

    # 生成交易信号
    data = generate_signals(data)

    # 绘制结果
    plot_results(data)
