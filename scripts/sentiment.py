import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns


# def numberOfArticlesWithSentimentAnalysis(news_data):
#     # Check for missing values or invalid categories
#     if 'sentiment_score_word' not in news_data.columns:
#         print("Error: 'sentiment_score_word' column not found.")
#         return
    
#     # Handle missing values
#     news_data = news_data.dropna(subset=['sentiment_score_word'])

#     # Count sentiment categories
#     sentiment_counts = news_data['sentiment_score_word'].value_counts().sort_index()

#     # Define colors for each category
#     colors = {'positive': 'green', 'negative': 'red', 'neutral': 'blue'}

#     # Create the bar plot with specified colors
#     sentiment_counts.plot(kind="bar", figsize=(10, 4), title='Sentiment Analysis',
#                         xlabel='Sentiment categories', ylabel='Number of Published Articles',
#                         color=[colors.get(category, 'gray') for category in sentiment_counts.index])

#     # Display the plot
#     plt.show()


from textblob import TextBlob
import pandas as pd

def analyze_and_display_sentiment(df, text_column):
    """
    Analyzes the sentiment of text in the specified column of a DataFrame, adds a sentiment score column, and displays the DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the text data.
    - text_column (str): The name of the column containing text data for sentiment analysis.
    """
    # Function to get sentiment score
    def get_sentiment(text):
        analysis = TextBlob(text)
        return analysis.sentiment.polarity

    # Apply sentiment analysis to the specified column
    df['sentiment'] = df[text_column].apply(get_sentiment)

    # Display the DataFrame with sentiment scores
    print(df[[text_column, 'sentiment']].head())


def plot_correlation_heatmap(correlation_matrix):
    """
    Plot a correlation heatmap.

    Parameters:
    - correlation_matrix: DataFrame, the correlation matrix to be visualized

    Returns:
    - None, displays the heatmap
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Heatmap')
    plt.show()