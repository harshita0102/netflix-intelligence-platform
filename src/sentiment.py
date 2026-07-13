"""
Netflix Intelligence Platform
Sentiment Analysis

Author: Harshita Agarwal
"""

import pandas as pd
import plotly.express as px
from textblob import TextBlob


class NetflixSentiment:

    def __init__(self, filepath):

        self.df = pd.read_csv(filepath)

    # ----------------------------
    # Calculate Sentiment
    # ----------------------------
    def calculate_sentiment(self):

        print("Calculating Sentiment...")

        self.df["description"] = self.df["description"].fillna("")

        polarity = []

        sentiment = []

        for text in self.df["description"]:

            score = TextBlob(text).sentiment.polarity

            polarity.append(score)

            if score > 0:

                sentiment.append("Positive")

            elif score < 0:

                sentiment.append("Negative")

            else:

                sentiment.append("Neutral")

        self.df["Polarity"] = polarity

        self.df["Sentiment"] = sentiment

        print("Done!")

    # ----------------------------
    # Pie Chart
    # ----------------------------
    def pie_chart(self):

        data = self.df["Sentiment"].value_counts()

        fig = px.pie(
            values=data.values,
            names=data.index,
            title="Sentiment Distribution",
            hole=0.5
        )

        fig.show()

    # ----------------------------
    # Histogram
    # ----------------------------
    def histogram(self):

        fig = px.histogram(
            self.df,
            x="Polarity",
            nbins=40,
            title="Polarity Score Distribution"
        )

        fig.show()

    # ----------------------------
    # Most Positive Titles
    # ----------------------------
    def positive_titles(self):

        print("\nTop Positive Descriptions\n")

        top = self.df.sort_values(
            "Polarity",
            ascending=False
        )

        print(top[["title", "Polarity"]].head(10))

    # ----------------------------
    # Most Negative Titles
    # ----------------------------
    def negative_titles(self):

        print("\nTop Negative Descriptions\n")

        low = self.df.sort_values(
            "Polarity"
        )

        print(low[["title", "Polarity"]].head(10))

    # ----------------------------
    # Save
    # ----------------------------
    def save(self):

        self.df.to_csv(
            "dataset/netflix_sentiment.csv",
            index=False
        )

        print("\nSentiment Dataset Saved!")

    # ----------------------------
    # Run
    # ----------------------------
    def run(self):

        self.calculate_sentiment()

        self.pie_chart()

        self.histogram()

        self.positive_titles()

        self.negative_titles()

        self.save()


if __name__ == "__main__":

    sentiment = NetflixSentiment(
        "dataset/cleaned_netflix.csv"
    )

    sentiment.run()