"""
Netflix Intelligence Platform
Movie Recommendation System

Author: Harshita Agarwal
"""

import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class NetflixRecommendation:

    def __init__(self, filepath):

        self.df = pd.read_csv(filepath)

        self.vectorizer = None

        self.similarity = None

    # ---------------------------------
    # Prepare Data
    # ---------------------------------
    def prepare(self):

        print("Preparing Dataset...")

        self.df["description"] = self.df["description"].fillna("")

        self.vectorizer = TfidfVectorizer(stop_words="english")

        tfidf_matrix = self.vectorizer.fit_transform(self.df["description"])

        self.similarity = cosine_similarity(tfidf_matrix)

        print("Recommendation Model Ready!")

    # ---------------------------------
    # Recommend Movies
    # ---------------------------------
    def recommend(self, movie_name, top_n=5):

        movie_name = movie_name.lower()

        titles = self.df["title"].str.lower()

        if movie_name not in titles.values:

            print("\nMovie Not Found!")

            return

        index = titles[titles == movie_name].index[0]

        scores = list(enumerate(self.similarity[index]))

        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        print("\nRecommended Titles\n")

        count = 0

        for i in scores[1:]:

            print(self.df.iloc[i[0]]["title"])

            count += 1

            if count == top_n:
                break

    # ---------------------------------
    # Save Model
    # ---------------------------------
    def save_model(self):

        with open("models/similarity.pkl", "wb") as f:
            pickle.dump(self.similarity, f)

        with open("models/vectorizer.pkl", "wb") as f:
            pickle.dump(self.vectorizer, f)

        print("\nModels Saved Successfully!")

    # ---------------------------------
    # Run
    # ---------------------------------
    def run(self):

        self.prepare()

        while True:

            movie = input("\nEnter Movie Name (or 'exit'): ")

            if movie.lower() == "exit":
                break

            self.recommend(movie)


if __name__ == "__main__":

    recommender = NetflixRecommendation(
        "dataset/cleaned_netflix.csv"
    )

    recommender.run()