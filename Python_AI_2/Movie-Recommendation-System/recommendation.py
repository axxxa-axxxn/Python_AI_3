import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:

    def __init__(self, csv_file):
        self.movies = pd.read_csv(csv_file)

        vectorizer = CountVectorizer()

        genre_matrix = vectorizer.fit_transform(
            self.movies["genre"]
        )

        self.similarity = cosine_similarity(
            genre_matrix
        )

    def recommend(self, movie_title, num_recommendations=5):

        movie_title = movie_title.lower()

        matching_movies = self.movies[
            self.movies["title"].str.lower() == movie_title
        ]

        if matching_movies.empty:
            return None

        movie_index = matching_movies.index[0]

        similarity_scores = list(
            enumerate(self.similarity[movie_index])
        )

        similarity_scores = sorted(
            similarity_scores,
            key=lambda x: x[1],
            reverse=True
        )

        recommendations = []

        for i in similarity_scores[1:num_recommendations + 1]:

            recommendations.append(
                self.movies.iloc[i[0]]["title"]
            )

        return recommendations