
import streamlit as st
import pickle
import pandas as pd
import requests
import time


from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()

retry = Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504]
)

adapter = HTTPAdapter(max_retries=retry)
session.mount("https://", adapter)


def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=53ab9fa13e5924cfc7d2ed573a5800ba&language=en-US"

        response = session.get(
            url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        data = response.json()

        if data.get("poster_path"):
            return "https://image.tmdb.org/t/p/w500" + data["poster_path"]

        return None

    except:
        return None


 #def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=53ab9fa13e5924cfc7d2ed573a5800ba&language=en-US".format(movie_id))
    data = response.json()

    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters =[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        # st.write("Movie ID =", movie_id)#
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        poster = fetch_poster(movie_id)
        recommended_movies_posters.append(poster)

        time.sleep(1)
    return recommended_movies,recommended_movies_posters
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
# movies_list = movies_list["title"].values
movies = pd.DataFrame(movies_dict)
#st.write(movies.head())#
#st.write(movies.columns)#
similarity = pickle.load(open("similarity.pkl", "rb"))
st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Movies",movies["title"].values
)


if st.button("Recommend"):
    names,posters = recommend(selected_movie_name)

    col1, col2 ,col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        if posters[0]:
            st.image(posters[0], use_container_width=True)
        else:
            st.write("Poster not available")

    with col2:
        st.text(names[1])
        if posters[1]:
            st.image(posters[1], use_container_width=True)
        else:
            st.write("Poster not available")

    with col3:
        st.text(names[2])
        if posters[2]:
            st.image(posters[2], use_container_width=True)
        else:
            st.write("Poster not available")

    with col4:
        st.text(names[3])
        if posters[3]:
            st.image(posters[3], use_container_width=True)
        else:
            st.write("Poster not available")

    with col5:
        st.text(names[4])
        if posters[4]:
            st.image(posters[4], use_container_width=True)
        else:
            st.write("Poster not available")

