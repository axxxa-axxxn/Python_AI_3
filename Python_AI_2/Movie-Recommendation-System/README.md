# 🎬 Movie Recommendation System

A Python-based Movie Recommendation System that suggests similar movies based on user input. The project uses Machine Learning techniques with Scikit-Learn and integrates with the TMDB API to fetch movie details such as ratings, release dates, descriptions, and posters.

## Features

* Movie recommendations based on genre similarity
* TMDB API integration
* Movie ratings and release dates
* Movie descriptions (overview)
* Movie poster display
* Command-line interface
* Streamlit web application

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Requests
* Streamlit
* TMDB API

## Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── api.py
├── main.py
├── recommendation.py
├── movies.csv
├── requirements.txt
├── README.md
└── venv/
```

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd Movie-Recommendation-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## TMDB API Setup

1. Create an account on TMDB.
2. Generate an API key.
3. Open `api.py`.
4. Replace:

```python
API_KEY = "YOUR_TMDB_API_KEY"
```

with your own API key.

## Running the Application

### Terminal Version

```bash
python main.py
```

### Streamlit Web App

```bash
streamlit run app.py
```

Open the URL shown in the terminal (usually http://localhost:8501).

## Example

Input:

```text
Interstellar
```

Output:

```text
Recommended Movies:
- Inception
- The Matrix
- Avatar
- Guardians of the Galaxy
```
## Author

Ayela Ahsan

## License

This project is developed for educational and learning purposes.
