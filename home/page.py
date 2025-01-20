import streamlit as st
import plotly.express as px
from movies.service import MovieService


def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    st.title('Estatísticas de FIlmes')

    if len(movie_stats['movies_by_genre']) > 0:
        st.subheader('Porcentagem de Filmes por Gênero')
        fig = px.pie(
            movie_stats['movies_by_genre'],
            values='count',
            names='genre__name',
        )
        st.plotly_chart(fig)

    """st.subheader('Total de Filmes Cadastrados:')
    st.write(movie_stats['total_movies'])"""

    st.subheader('Quantidade de FIlmes por Gênero:')
    fig = px.bar(
        movie_stats['movies_by_genre'],
        x='genre__name',
        y='count',
        labels={'genre__name': 'Gênero', 'count': 'Quantidade'},
        color='genre__name'
    )
    st.plotly_chart(fig)

    st.subheader('Estatísticas Gerais:')
    stats = {
        'Total de Filmes': movie_stats['total_movies'],
        'Total de Avaliações': movie_stats['total_reviews'],
        'Média de Estrelas': movie_stats['average_stars']
    }
    fig = px.bar(
        x=list(stats.keys()),
        y=list(stats.values()),
        labels={'x': 'Métrica', 'y': 'Valor'},
        color=list(stats.keys())
    )
    st.plotly_chart(fig)