import yfinance as yf
import matplotlib.pyplot as plt

tickers = ["JPM", "DIS", "WMT", "MCD", "KO", "PG"]

start_date = "2018-01-01"
end_date = "2021-12-31"
data = yf.download(tickers, start=start_date, end=end_date)["Adj Close"]

for ticker in tickers:
    data[ticker + '_Returns'] = data[ticker].pct_change()

short_window = 50
long_window = 200
bollinger_window = 20
num_std = 2
rsi_window = 14

for ticker in tickers:
    plt.figure(figsize=(12, 12))

    data[ticker + '_Short_MA'] = data[ticker].rolling(window=short_window).mean()
    data[ticker + '_Long_MA'] = data[ticker].rolling(window=long_window).mean()

    data[ticker + '_MA_Signal'] = 0
    data.loc[data[ticker + '_Short_MA'] > data[ticker + '_Long_MA'], ticker + '_MA_Signal'] = 1
    data.loc[data[ticker + '_Short_MA'] < data[ticker + '_Long_MA'], ticker + '_MA_Signal'] = -1

    rolling_mean = data[ticker].rolling(window=bollinger_window).mean()
    rolling_std = data[ticker].rolling(window=bollinger_window).std()
    data[ticker + '_Upper_Band'] = rolling_mean + num_std * rolling_std
    data[ticker + '_Lower_Band'] = rolling_mean - num_std * rolling_std

    data[ticker + '_Bollinger_Signal'] = 0
    data.loc[data[ticker] < data[ticker + '_Lower_Band'], ticker + '_Bollinger_Signal'] = 1
    data.loc[data[ticker] > data[ticker + '_Upper_Band'], ticker + '_Bollinger_Signal'] = -1

    delta = data[ticker].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=rsi_window).mean()
    avg_loss = loss.rolling(window=rsi_window).mean()
    rs = avg_gain / avg_loss
    data[ticker + '_RSI'] = 100 - (100 / (1 + rs))

    data[ticker + '_RSI_Signal'] = 0
    data.loc[(data[ticker + '_RSI'] < 30) & (data[ticker + '_RSI'].shift(1) >= 30), ticker + '_RSI_Signal'] = 1
    data.loc[(data[ticker + '_RSI'] > 70) & (data[ticker + '_RSI'].shift(1) <= 70), ticker + '_RSI_Signal'] = -1

    data[ticker + '_MA_Cumulative_Returns'] = (1 + data[ticker + '_MA_Signal'].shift(1) * data[ticker + '_Returns']).cumprod()
    data[ticker + '_Bollinger_Cumulative_Returns'] = (1 + data[ticker + '_Bollinger_Signal'].shift(1) * data[ticker + '_Returns']).cumprod()
    data[ticker + '_RSI_Cumulative_Returns'] = (1 + data[ticker + '_RSI_Signal'].shift(1) * data[ticker + '_Returns']).cumprod()

    plt.subplot(4, 1, 1)
    plt.plot(data.index, data[ticker], label='Price', color='black')
    plt.plot(data.index, data[ticker + '_Short_MA'], label='Short MA', color='blue', linestyle='dashed')
    plt.plot(data.index, data[ticker + '_Long_MA'], label='Long MA', color='red', linestyle='dashed')
    plt.legend()
    plt.title(f'{ticker} Trading Strategies')
    plt.ylabel('Price')
    plt.xticks([])

    plt.subplot(4, 1, 2)
    plt.plot(data.index, data[ticker], label='Price', color='black')
    plt.plot(data.index, data[ticker + '_Upper_Band'], label='Upper Bollinger Band', color='blue', linestyle='dashed')
    plt.plot(data.index, data[ticker + '_Lower_Band'], label='Lower Bollinger Band', color='red', linestyle='dashed')
    plt.legend()
    plt.ylabel('Price')
    plt.xticks([])

    plt.subplot(4, 1, 3)
    plt.plot(data.index, data[ticker + '_RSI'], label='RSI', color='purple')
    plt.axhline(y=70, color='red', linestyle='dashed', label='Overbought (70)')
    plt.axhline(y=30, color='green', linestyle='dashed', label='Oversold (30)')
    plt.legend()
    plt.ylabel('RSI')

    plt.subplot(4, 1, 4)
    plt.plot(data.index, data[ticker + '_MA_Cumulative_Returns'], label='Moving Average Strategy', color='blue')
    plt.plot(data.index, data[ticker + '_Bollinger_Cumulative_Returns'], label='Bollinger Bands Strategy', color='green')
    plt.plot(data.index, data[ticker + '_RSI_Cumulative_Returns'], label='RSI Strategy', color='purple')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')

    plt.tight_layout()
    plt.savefig(f"{ticker}_trading_strategies.png")
