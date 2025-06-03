Overview
This project integrates financial market data with news sentiment analysis to explore the relationship between market behavior and public sentiment. It leverages Python for data manipulation, analysis, and visualization, combining historical stock data with natural language processing to generate insights into:
* Price movements and technical stock indicators
* Sentiment trends from news articles
* Portfolio performance optimization
The workflow involves
1. Data Loading: Load historical stock data and news articles.
2. Sentiment Analysis: Analyze headlines/text from news articles to extract sentiment polarity scores using TextBlob.
3. Stock Technical Analysis: Compute technical indicators (SMA, RSI, EMA, MACD) to track stock performance.
4. Portfolio Optimization: Analyze stock price data to optimize portfolio weights, calculate returns, and compare stock indicators.
Key Functions Overview
1. Data Loading and Sentiment Analysis
loadHistoricalData(ticker)
Loads historical stock data for a given ticker symbol from a CSV file.
get_sentiment(text)
Analyzes sentiment of text (news headlines) using TextBlob and returns a polarity score.
numberOfArticlesWithSentimentAnalysis(news_data)
Analyzes the sentiment distribution of news articles and creates a bar chart showing the count of positive, neutral, and negative sentiments.
getSentimentAnalysisOfPublisher(news_data, target_publisher)
Produces a bar chart of sentiment distribution (positive, neutral, negative) for news articles.
2. Data Quality and Descriptive Analysis
checkMissingValueOfHistoricalDataset(stock_data...)
Checks for missing values in historical datasets for multiple stocks and summarizes the results.
calculateDescriptiveStatisticsOfHistoricalData(stock_data ...)
Computes and displays descriptive statistics (mean, std dev, min, max) for closing prices across different stocks.
3. Time Series and Stock Analysis
analysisClosingPriceWithDate(stock_data...)
Creates time series plots for closing prices to observe stock trends over time.
calculateTechnicalIndicator(stock_data)
Computes essential technical indicators for a stock, including:
* Simple Moving Average (SMA)
* Relative Strength Index (RSI)
* Exponential Moving Average (EMA)
* Moving Average Convergence Divergence (MACD)
* Adds them as new columns to the stock dataset.
* technicalIndicatorsVsClosingPrice(stock_data... ticker):Compares stock closing prices with chosen technical indicators over time using line plots.
* ClosingPriceRelativeStrengthIndex(stock_data, ...) Visualizes RSI alongside closing prices, identifying overbought/oversold conditions.
* closingPriceMovingAverageConvergenceDivergence(stock_data_aapl, stock_data_amzn, ..., stock_data_nvda) Creates time series plots for closing prices with the MACD indicator to analyze price momentum and trends.
4. Portfolio Analysis
* calculate PortfolioWeightAndPerformance(): Optimizes portfolio weights using historical stock returns and analyzes the portfolio's risk and return performance.
Tools and Libraries Used
* Pandas: For data loading, preprocessing, and analysis
* TextBlob: Sentiment analysis of news articles.
* TA-Lib: For technical indicators (SMA, RSI, EMA, MACD).
* yfinance: Fetching historical market data for various stocks.
* Matplotlib/Seaborn: For visualizations such as time series, bar charts, and scatter plots.
