from recommendation import MovieRecommender
from api import get_movie_details


def main():

    recommender = MovieRecommender("movies.csv")

    print("=" * 50)
    print("MOVIE RECOMMENDATION SYSTEM")
    print("=" * 50)

    while True:

        movie_name = input(
            "\nEnter a movie name (or quit): "
        )

        if movie_name.lower() == "quit":
            print("\nThank you for using the Movie Recommendation System!")
            break

        recommendations = recommender.recommend(
            movie_name
        )

        if recommendations is None:
            print("\nMovie not found.")
        else:
            print("\nRecommended Movies:\n")

            for movie in recommendations:

                details = get_movie_details(movie)

                if details:

                    print(f"Title  : {details['title']}")
                    print(f"Rating : {details['rating']}")
                    print(f"Release: {details['release_date']}")
                    print("-" * 50)

                else:
                    print(f"Title  : {movie}")
                    print("Details not available.")
                    print("-" * 50)


if __name__ == "__main__":
    main()