import sqlite3
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_netflix.csv")

# Create SQLite database
conn = sqlite3.connect("dataset/netflix.db")

# Export dataframe to SQL table
df.to_sql(
    "netflix",
    conn,
    if_exists="replace",
    index=False
)

print("Database Created Successfully!")

conn.close()