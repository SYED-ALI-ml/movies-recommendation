import streamlit as st 
import pickle 
import pandas as pd 
from importnb import imports
import numpy as np # type: ignore
import pandas as pd # type: ignore
# import ast
# import nltk
# from sklearn.feature_extraction.text import CountVectorize
import pandas 

movies_df = pd.read_csv('movies_with_posters.csv')


with imports("ipynb"):
    import movies_recommnder_system # type: ignore

recommend = movies_recommnder_system.recommend
id = movies_recommnder_system.id_fetecher_image
overview_movie_  = movies_recommnder_system.movie_overview
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title("Movie Recommender System")


selected_movie_name  = st.selectbox("Recommended Movies", movies['title'].values)

if st.button('Recommend') :
    if selected_movie_name :
        names = recommend(selected_movie_name)
        posters = id(selected_movie_name)
        overview_movie = overview_movie_(selected_movie_name)
        if names and posters:
            cols = st.columns(15)

            for i in range(len(names)):
                col1, col2 = st.columns([1, 2])  # Adjust the width ratio as needed
                
                with col1:
                    st.image(posters[i], use_column_width=True)
                
                with col2:
                    st.write(f"### {names[i]}")
                    st.write(f"Additional information :")
                    st.write(overview_movie[i])
    else :
        st.write("Movie not found, please try again.")
        
else: 

    num_movies = min(50, len(movies_df)) 

    cols_per_row = 5
    rows = (num_movies + cols_per_row - 1) // cols_per_row
    movies_to_display = movies_df.head(num_movies)

    for row in range(rows):
        cols = st.columns(cols_per_row)
        for i in range(cols_per_row):
            movie_index = row * cols_per_row + i
            if movie_index < num_movies:
                with cols[i]:
                    movie = movies_to_display.iloc[movie_index]
                    st.image(movie['poster_url'], use_column_width=True)
                    st.write(movie['title'])

    