import streamlit as st
import pickle

def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True,

                             key=lambda x: x[1])[1:6]
        recommend_movies = []
        for i in movies_list:
            recommend_movies.append(movies.iloc[i[0]].title)
            return recommend_movies


movies_d = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = movies['title'].values
st.title('Movie Recommender')
selectedMovieName = st.selectbox(
    "Search Here",
    movies
)
if st.button('Show Results'):
    recommendations = recommend(selectedMovieName)
    for i in recommendations:
     st.write(i)




