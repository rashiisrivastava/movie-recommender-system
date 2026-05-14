# Movie Recommender System

A Content-Based Movie Recommender System built using **Python**, **Machine Learning**, and **Streamlit** that recommends similar movies based on user selection and displays movie posters using the **OMDb API**.

---

# Features

- Recommend top 5 similar movies
- Interactive web application using Streamlit
- Movie posters fetched using OMDb API
- Fast and efficient recommendation system
- Clean and user-friendly interface

---

# Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle
- Requests
- OMDb API

---

# Dataset

This project uses the TMDB 5000 Movies Dataset.

Files used:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

---

# Machine Learning Approach

This project uses **Content-Based Filtering**.

Movie features such as:
- Genres
- Keywords
- Cast
- Crew
- Overview

are combined into tags and converted into vectors using text vectorization techniques.  
Cosine similarity is then used to find similar movies.

---

# API Used

This project uses the OMDb API for fetching movie posters.

---

# How It Works

- User selects a movie from the dropdown.
- The system calculates similarity scores using cosine similarity.
- Top 5 similar movies are selected.
- Posters are fetched using the OMDb API.
- Recommendations are displayed on the Streamlit interface.

---
<img width="1914" height="944" alt="image" src="https://github.com/user-attachments/assets/27c66b9f-6256-422c-93e1-bfc2e58ec308" />
