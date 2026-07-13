"""
Netflix Intelligence Platform
EDA Module

Author: Harshita Agarwal
"""

import pandas as pd
import plotly.express as px
import os


class NetflixEDA:

    def __init__(self, filepath):

        self.df = pd.read_csv(filepath)

    # -------------------------
    # Dataset Overview
    # -------------------------
    def overview(self):

        print("="*50)
        print("NETFLIX DATASET OVERVIEW")
        print("="*50)

        print(f"Rows : {self.df.shape[0]}")
        print(f"Columns : {self.df.shape[1]}")

        print("\nColumns")

        print(self.df.columns)

    # -------------------------
    # Movies vs TV Shows
    # -------------------------
    def movies_vs_tv(self):

        data = self.df["type"].value_counts()

        fig = px.pie(
            values=data.values,
            names=data.index,
            title="Movies vs TV Shows",
            hole=0.45
        )

        fig.show()

    # -------------------------
    # Top Countries
    # -------------------------
    def top_countries(self):

        countries = (
            self.df["country"]
            .str.split(",")
            .explode()
            .str.strip()
            .value_counts()
            .head(10)
        )

        fig = px.bar(
            x=countries.index,
            y=countries.values,
            color=countries.values,
            title="Top 10 Countries"
        )

        fig.show()

    # -------------------------
    # Top Genres
    # -------------------------
    def top_genres(self):

        genres = (
            self.df["listed_in"]
            .str.split(",")
            .explode()
            .str.strip()
            .value_counts()
            .head(15)
        )

        fig = px.bar(
            x=genres.index,
            y=genres.values,
            color=genres.values,
            title="Top 15 Genres"
        )

        fig.show()

    # -------------------------
    # Ratings
    # -------------------------
    def ratings(self):

        rating = self.df["rating"].value_counts()

        fig = px.bar(
            x=rating.index,
            y=rating.values,
            color=rating.values,
            title="Netflix Ratings Distribution"
        )

        fig.show()

    # -------------------------
    # Top Directors
    # -------------------------
    def top_directors(self):

        directors = (
            self.df[self.df["director"] != "Unknown"]["director"]
            .value_counts()
            .head(10)
        )

        fig = px.bar(
            x=directors.index,
            y=directors.values,
            color=directors.values,
            title="Top Directors"
        )

        fig.show()

    # -------------------------
    # Release Trend
    # -------------------------
    def release_trend(self):

        release = (
            self.df["release_year"]
            .value_counts()
            .sort_index()
        )

        fig = px.line(
            x=release.index,
            y=release.values,
            markers=True,
            title="Release Trend"
        )

        fig.show()

    # -------------------------
    # Year Added Trend
    # -------------------------
    def year_added(self):

        year = (
            self.df["Year Added"]
            .value_counts()
            .sort_index()
        )

        fig = px.area(
            x=year.index,
            y=year.values,
            title="Content Added Per Year"
        )

        fig.show()

    # -------------------------
    # Top Actors
    # -------------------------
    def top_actors(self):

        actors = (
            self.df["cast"]
            .str.split(",")
            .explode()
            .str.strip()
            .value_counts()
            .head(15)
        )

        fig = px.bar(
            x=actors.index,
            y=actors.values,
            color=actors.values,
            title="Top Actors"
        )

        fig.show()

    # -------------------------
    # Movie Duration
    # -------------------------
    def movie_duration(self):

        movie = self.df[self.df["type"] == "Movie"]

        fig = px.histogram(
            movie,
            x="Movie Duration",
            nbins=30,
            title="Movie Duration Distribution"
        )

        fig.show()

    # -------------------------
    # Monthly Trend
    # -------------------------
    def monthly_content(self):

        order = [
            "January","February","March","April",
            "May","June","July","August",
            "September","October","November","December"
        ]

        month = (
            self.df["Month Added"]
            .value_counts()
            .reindex(order)
        )

        fig = px.line(
            x=month.index,
            y=month.values,
            markers=True,
            title="Monthly Content Addition"
        )

        fig.show()

    # -------------------------
    # KPI Dashboard
    # -------------------------
    def dashboard(self):

        total_titles = len(self.df)

        movies = len(self.df[self.df["type"]=="Movie"])

        tv = len(self.df[self.df["type"]=="TV Show"])

        countries = (
            self.df["country"]
            .str.split(",")
            .explode()
            .str.strip()
            .nunique()
        )

        genres = (
            self.df["listed_in"]
            .str.split(",")
            .explode()
            .str.strip()
            .nunique()
        )

        print("="*50)
        print("NETFLIX KPI DASHBOARD")
        print("="*50)

        print(f"Total Titles : {total_titles}")

        print(f"Movies : {movies}")

        print(f"TV Shows : {tv}")

        print(f"Countries : {countries}")

        print(f"Genres : {genres}")

        print(f"Average Release Year : {round(self.df['release_year'].mean())}")

        print("="*50)

    # -------------------------
    # Run All
    # -------------------------
    def run(self):

        self.overview()

        self.dashboard()

        self.movies_vs_tv()

        self.top_countries()

        self.top_genres()

        self.ratings()

        self.top_directors()

        self.release_trend()

        self.year_added()

        self.top_actors()

        self.movie_duration()

        self.monthly_content()


if __name__ == "__main__":

    filepath = "dataset/cleaned_netflix.csv"

    eda = NetflixEDA(filepath)

    eda.run()