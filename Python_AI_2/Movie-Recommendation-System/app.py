import streamlit as st
from recommendation import MovieRecommender
from api import get_movie_details

recommender = MovieRecommender("movies.csv")

st.title("🎬 Movie Recommendation System")

movie_name = st.text_input("Enter Movie Name")

if st.button("Recommend"):

    recommendations = recommender.recommend(movie_name)

    if recommendations is None:
        st.error("Movie not found!")

    else:
        st.subheader("Recommended Movies")

        for movie in recommendations:

            details = get_movie_details(movie)

            if details:

                st.write(f"## {details['title']}")

                if details["poster"]:
                    st.image(details["poster"], width=200)

                st.write(f"⭐ Rating: {details['rating']}")
                st.write(f"📅 Release Date: {details['release_date']}")
                st.write(details["overview"])

                st.divider()