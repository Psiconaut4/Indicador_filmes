import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

api_key = '0e823fa4f05de457b82c68d49a60dbb3'
analyzer = SentimentIntensityAnalyzer()


def suggest_movies(i):
    phrase = i
    emotion = analyzer.polarity_scores(phrase)['compound']

    if emotion <= -0.5:
        genre = '27'  # horror
    elif emotion >= 0.5 and emotion < 0.6:
        genre = '35'  # Comédia
    elif emotion > 0.6 and emotion < 1.0:
        genre = '10749'  # Romance
    elif emotion > -0.5 and emotion < 0.3:
        genre = '18'  # drama

    url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&sort_by=popularity.desc&with_genres={genre}&vote_count.gte=4'
    response = requests.get(url).json()


    if response['results']:

        # pegando os titulos
        titles = [result['title'] for result in response['results'][:3]]

        # pegando as datas
        release_date = [result['release_date'] for result in response['results'][:3]]

        # pegando os votos
        vote_average = [result['vote_average'] for result in response['results'][:3]]

        # pegando os posters/ definindo a string do prefixo
        prefix = 'https://media.themoviedb.org/t/p/w220_and_h330_face/'
        poster_path = [prefix + result['poster_path'].lstrip('/') for result in response['results'][:3]]

        # retornando os resultados como lista
        return [titles, poster_path, release_date, vote_average]
