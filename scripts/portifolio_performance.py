import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from textblob import TextBlob
import talib as tl

def loadHistoricalData(ticker):
    stock_data=pd.read_csv(f'./Data/yfinance_data/{ticker}_historical_data.csv')
    return stock_data
def calculatePortfolioWeightAndPerformance():
    from pypfopt.efficient_frontier import EfficientFrontier
    from pypfopt import risk_models
    from pypfopt import expected_returns

    tickers =['AAPL','AMZN','GOOG','MSFT','NVDA','META','TSLA']
    # Load data from each ticker file
    dataframes = [loadHistoricalData(ticker) for ticker in tickers]

    # Combine dataframes into a single DataFrame
    combined_data = pd.concat(dataframes, axis=1)['Close']

    new_column_names = ['AAPL', 'AMZN','GOOG', 'META','MSFT','NVDA','TSLA'] 
    combined_data.columns = new_column_names

    # Calculate expected returns and sample covariance
    mu = expected_returns.mean_historical_return(combined_data)
    S = risk_models.sample_cov(combined_data)

    # Optimize for maximal Sharpe ratio
    ef = EfficientFrontier(mu, S)
    weights = ef.max_sharpe()
    weights = dict(zip(['AAPL', 'AMZN','GOOG', 'META','MSFT','NVDA','TSLA'],[round(value, 2) for value in weights.values()]))

    # Print Portfolio weights
    print("Portfolio Weights:")
    print(weights)
    # Calculate and print portfolio performance
    print("\nPortfolio Performance:")
    ef.portfolio_performance(verbose=True)