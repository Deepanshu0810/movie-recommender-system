import streamlit as st
import pickle
import pandas as pd
import os
import requests
from dotenv import load_dotenv

load_dotenv()


api = os.getenv('APIKEY')
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies_dict = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

def poster(id):
    url='https://api.themoviedb.org/3/movie/{}?api_key={}'.format(id,api)
    response = requests.get(url)
    data = response.json()
    poster_url = "http://image.tmdb.org/t/p/w500"+data['poster_path']
    return poster_url
    
def recommend(movie):
    i = movies_dict[movies_dict['title']==movie].index[0]
    movies = sorted(list(enumerate(similarity[i])),reverse=True,key=lambda x:x[1])[1:6]
    l = list()
    posters = list()
    for m in movies:
        id = movies_dict.iloc[m[0]].id
        posters.append(poster(id))
        l.append(movies_dict.iloc[m[0]].title)
    return l,posters

st.title("Movie Recommender System")
option = st.selectbox(
        "Please select a Movie",
        movies_dict['title'].values,
    )

if st.button('Get Rcommendations'):
    recommendations, movie_poster = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommendations[0])
        st.image(movie_poster[0])
    with col2:
        st.text(recommendations[1])
        st.image(movie_poster[1])
    with col3:
        st.text(recommendations[2])
        st.image(movie_poster[2])
    with col4:
        st.text(recommendations[3])
        st.image(movie_poster[3])
    with col5:
        st.text(recommendations[4])
        st.image(movie_poster[4])