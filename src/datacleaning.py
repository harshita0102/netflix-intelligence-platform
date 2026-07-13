import pandas as pd
import os


class NetflixDataCleaner:

    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    # ------------------------
    # Load Dataset
    # ------------------------
    def load_data(self):

        print("Loading Dataset...")

        self.df = pd.read_csv(self.filepath)

        print("Dataset Loaded Successfully!")

        print(self.df.shape)

        return self.df

    # ------------------------
    # Dataset Info
    # ------------------------
    def dataset_summary(self):

        print("\nShape")

        print(self.df.shape)

        print("\nColumns")

        print(self.df.columns)

        print("\nMissing Values")

        print(self.df.isnull().sum())

        print("\nDuplicate Rows")

        print(self.df.duplicated().sum())

    # ------------------------
    # Remove Duplicates
    # ------------------------
    def remove_duplicates(self):

        self.df.drop_duplicates(inplace=True)

        print("\nDuplicates Removed")

    # ------------------------
    # Missing Values
    # ------------------------
    def clean_missing_values(self):

        self.df["director"] = self.df["director"].fillna("Unknown")

        self.df["cast"] = self.df["cast"].fillna("Unknown")

        self.df["country"] = self.df["country"].fillna("Unknown")

        self.df["rating"] = self.df["rating"].fillna("Not Rated")

        self.df["description"] = self.df["description"].fillna("No Description")

        self.df["date_added"] = self.df["date_added"].astype(str).str.strip()

        self.df["date_added"] = pd.to_datetime(
            self.df["date_added"],
            errors="coerce"
        )

        self.df.dropna(subset=["date_added"], inplace=True)

        print("\nMissing Values Cleaned")

    # ------------------------
    # Feature Engineering
    # ------------------------
    def feature_engineering(self):

        self.df["Year Added"] = self.df["date_added"].dt.year

        self.df["Month Added"] = self.df["date_added"].dt.month_name()

        self.df["Day Added"] = self.df["date_added"].dt.day_name()

        movie_mask = self.df["type"] == "Movie"

        tv_mask = self.df["type"] == "TV Show"

        self.df["Movie Duration"] = None

        self.df["TV Seasons"] = None

        self.df.loc[movie_mask, "Movie Duration"] = (
            self.df.loc[movie_mask, "duration"]
            .str.replace(" min", "", regex=False)
        )

        self.df.loc[tv_mask, "TV Seasons"] = (
            self.df.loc[tv_mask, "duration"]
            .str.replace(" Seasons", "", regex=False)
            .str.replace(" Season", "", regex=False)
        )

        self.df["Movie Duration"] = pd.to_numeric(
            self.df["Movie Duration"],
            errors="coerce"
        )

        self.df["TV Seasons"] = pd.to_numeric(
            self.df["TV Seasons"],
            errors="coerce"
        )

        print("\nFeature Engineering Completed")

    # ------------------------
    # Save Dataset
    # ------------------------
    def save_dataset(self):

        output = "dataset/cleaned_netflix.csv"

        self.df.to_csv(output, index=False)

        print(f"\nDataset Saved At : {output}")

    # ------------------------
    # Run
    # ------------------------
    def run(self):

        self.load_data()

        self.dataset_summary()

        self.remove_duplicates()

        self.clean_missing_values()

        self.feature_engineering()

        self.save_dataset()


# ==========================
# MAIN
# ==========================

if __name__ == "__main__":

    dataset_path = "dataset/netflix_titles.csv"

    cleaner = NetflixDataCleaner(dataset_path)

    cleaner.run()