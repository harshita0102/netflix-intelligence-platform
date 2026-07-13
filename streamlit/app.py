import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Netflix Analytics Dashboard",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Netflix Analytics Dashboard")

df = pd.read_csv("dataset/netflix_titles.csv.zip")

st.success("Dataset Loaded Successfully!")

st.write(df.head())