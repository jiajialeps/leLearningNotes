import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# 获取历史数据
def get_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

# 计算移动平均线
def compute_moving_averages(data, short_window=20, long_window=50):
    data['Short_MA'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window, min_periods=1).mean()
    return data

# 生成交易信号
def generate_signals(data):
    data['Signal'] = 0
    data['Signal'][short_window:] = np.where(data['Short_MA'][short_window:] > data['Long_MA'][short_window:], 1, 0)
    data['Position'] = data['Signal'].diff()

    # 打印信号生成的调试信息
    print(data[['Close', 'Short_MA', 'Long_MA', 'Signal', 'Position']].tail(60))  # 打印最后60行数据

    return data

# 绘制结果
def plot_results(data):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price', alpha=0.5)
    plt.plot(data['Short_MA'], label='Short MA', alpha=0.75)
    plt.plot(data['Long_MA'], label='Long MA', alpha=0.75)

    # 买入信号
    buy_signals = data[data['Position'] == 1]
    sell_signals = data[data['Position'] == -1]

    plt.plot(buy_signals.index,
             buy_signals['Close'],
             '^', markersize=10, color='g', label='Buy Signal')

    plt.plot(sell_signals.index,
             sell_signals['Close'],
             'v', markersize=10, color='r', label='Sell Signal')

    plt.title('Moving Average Crossover Strategy')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()

# 主程序
if __name__ == "__main__":
    symbol = 'AAPL'  # 股票代码
    start_date = '2024-01-01'
    end_date = '2025-02-20'
    short_window = 20  # 短期移动平均线
    long_window = 50   # 长期移动平均线

    # 获取数据
    data = get_data(symbol, start_date, end_date)
    print(data.head())  # 打印数据的前几行

    # 计算移动平均线
    data = compute_moving_averages(data, short_window, long_window)
    print(data[['Close', 'Short_MA', 'Long_MA']].tail(60))  # 打印最后60行数据

    # 生成交易信号
    data = generate_signals(data)

    # 绘制结果
    plot_results(data)
