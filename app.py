import pickle
import streamlit as st
import requests

# Fetch poster from OMDb API
def fetch_poster(movie_name):
    try:
        url = f"http://www.omdbapi.com/?t={movie_name}&apikey=273a21f1"
        data = requests.get(url).json()

        if data['Response'] == 'True' and data['Poster'] != 'N/A':
            return data['Poster']
        else:
            return "https://via.placeholder.com/300x450?text=No+Poster"

    except:
        return "https://via.placeholder.com/300x450?text=Error"


# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:

        movie_name = movies.iloc[i[0]].title

        recommended_movie_names.append(movie_name)

        # Fetch poster using movie name
        recommended_movie_posters.append(fetch_poster(movie_name))

    return recommended_movie_names, recommended_movie_posters


# Streamlit UI
st.header('Movie Recommender System')

movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):

    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0], width=150)

    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1], width=150)

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2], width=150)

    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3], width=150)

    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4], width=150)