import streamlit as st
import pandas as pd
import plotly.express as px

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="Netflix Intelligence Platform",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Netflix Intelligence Platform")
st.markdown("Built with Python • Streamlit • Machine Learning")

# ---------------------------
# LOAD DATA
# ---------------------------

@st.cache_data
def load_data():
    return pd.read_csv("dataset/cleaned_netflix.csv")

df = load_data()

# ---------------------------
# SIDEBAR
# ---------------------------

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Recommendation System",
        "Dataset"
    ]
)

# =====================================================
# DASHBOARD
# =====================================================

if menu == "Dashboard":

    st.header("📊 Dashboard")

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Total Titles", len(df))

    col2.metric(
        "Movies",
        len(df[df["type"]=="Movie"])
    )

    col3.metric(
        "TV Shows",
        len(df[df["type"]=="TV Show"])
    )

    countries = (
        df["country"]
        .str.split(",")
        .explode()
        .str.strip()
        .nunique()
    )

    col4.metric(
        "Countries",
        countries
    )

    st.divider()

    # Movies vs TV

    type_count = df["type"].value_counts()

    fig = px.pie(
        values=type_count.values,
        names=type_count.index,
        title="Movies vs TV Shows",
        hole=0.5
    )

    st.plotly_chart(fig,use_container_width=True)

    # Top Genres

    genre = (
        df["listed_in"]
        .str.split(",")
        .explode()
        .str.strip()
        .value_counts()
        .head(10)
    )

    fig = px.bar(
        x=genre.index,
        y=genre.values,
        color=genre.values,
        title="Top Genres"
    )

    st.plotly_chart(fig,use_container_width=True)

    # Release Trend

    release = (
        df["release_year"]
        .value_counts()
        .sort_index()
    )

    fig = px.line(
        x=release.index,
        y=release.values,
        markers=True,
        title="Release Trend"
    )

    st.plotly_chart(fig,use_container_width=True)

# =====================================================
# RECOMMENDATION SYSTEM
# =====================================================

elif menu=="Recommendation System":

    st.header("🤖 Netflix Recommendation System")

    df["description"] = df["description"].fillna("")

    vectorizer = TfidfVectorizer(stop_words="english")

    matrix = vectorizer.fit_transform(df["description"])

    similarity = cosine_similarity(matrix)

    movie = st.selectbox(
        "Choose a Movie",
        sorted(df["title"].unique())
    )

    if st.button("Recommend"):

        index = df[df["title"]==movie].index[0]

        score = list(enumerate(similarity[index]))

        score = sorted(
            score,
            key=lambda x:x[1],
            reverse=True
        )

        st.success("Recommended Movies")

        for i in score[1:6]:

            st.write("🎬",df.iloc[i[0]]["title"])

# =====================================================
# DATASET
# =====================================================

else:

    st.header("📁 Dataset")

    st.dataframe(df)

    st.write("Rows :",df.shape[0])

    st.write("Columns :",df.shape[1])