# Automated Trading Algorithm Project

This project showcases an automated trading algorithm that leverages historical price data and technical indicators to generate trading signals and assess performance. The objective is to implement and analyze diverse trading strategies using Python and fundamental quantitative finance principles.

## Project Overview

In this project, we explore the application of automated trading strategies to a curated selection of stocks. We utilize historical stock price data from Yahoo Finance and implement three distinct trading strategies based on popular technical indicators: Moving Average Crossovers, Bollinger Bands, and the Relative Strength Index (RSI). Each strategy aims to exploit different market conditions and price trends.

## Key Features

- **Data Collection**: Obtain historical price data for a handpicked list of stocks using the `yfinance` Python library.

- **Technical Indicator Strategies**: Develop and implement the following trading strategies:
  - Moving Average Crossovers: Identify buy/sell signals based on short-term and long-term moving average crossovers.
  - Bollinger Bands: Utilize upper and lower thresholds to generate signals based on price volatility.
  - RSI Strategy: Apply the Relative Strength Index to pinpoint potential overbought and oversold conditions.

- **Signal Generation**: Calculate daily returns for each stock and utilize the selected trading strategies to produce buy/sell signals.

- **Interactive Visualizations**: Create informative visualizations using `matplotlib` to illustrate the effectiveness of each trading strategy:
  - Plot stock prices alongside short-term and long-term moving averages.
  - Visualize Bollinger Bands with upper and lower bounds.
  - Display the RSI indicator with designated overbought and oversold levels.

- **Cumulative Returns Analysis**: Compute and visualize cumulative returns for each trading strategy to assess their performance over the specified period.

## Insights and Analysis

- **Moving Average Crossovers**: This one tended to perform the best when given stocks with consistent growth, however was often slow to adjust to more rapid shifts in stock prices 

- **Bollinger Bands**: This one was able to capitalize somewhat on mean reversion tendencies, however was also slow to adjust and had the tendency to fall for false breakours

- **RSI Strategy**: This strategy often did the worst, given the stocks I chose, mostly because, as a strategy it performs poorly in highly trending markets, which for many of the stocks I chose (e.g tech stocks) fell into.

## Future Enhancements



### Advanced Strategy Combinations

I could explore the integration of more intricate trading strategies that combine multiple indicators and signals. By developing hybrid approaches that leverage a blend of moving average crossovers, Bollinger Bands, and RSI signals, I could generate more refined buy/sell signals. Incorporating various indicators might provide more robust and accurate trading decisions.

### Live Trading Integration

I could elevate the project's functionality from research and analysis to real-world trading by seamlessly integrating it with a trading platform or brokerage API. Implementing mechanisms to execute actual trades based on the generated signals, I could apply my strategies in live market conditions, gaining valuable experience in managing real trades and evaluating their performance.

### Machine Learning Optimization

I could leverage machine learning techniques to optimize trading strategies. By utilizing algorithms such as reinforcement learning, I could enable the strategy to adapt and fine-tune its parameters over time based on market feedback. Enabling the algorithm to learn from historical data, the strategy could potentially evolve and enhance its performance across different market conditions.
