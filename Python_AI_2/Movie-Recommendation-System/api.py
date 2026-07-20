import requests

API_KEY = "4b509088d1f7b45fa38eeb7905e282b7"


def get_movie_details(movie_name):

    url = (
        f"https://api.themoviedb.org/3/search/movie"
        f"?api_key={API_KEY}&query={movie_name}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    if not data["results"]:
        return None

    movie = data["results"][0]

    poster_path = movie.get("poster_path")

    poster_url = (
        f"https://image.tmdb.org/t/p/w500{poster_path}"
        if poster_path
        else "No Poster"
    )

    return {
        "title": movie["title"],
        "rating": movie["vote_average"],
        "release_date": movie["release_date"],
        "overview": movie["overview"],
        "poster": poster_url
    }