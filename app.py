import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

api_key = '0e823fa4f05de457b82c68d49a60dbb3'
analyzer = SentimentIntensityAnalyzer()


def suggest_movies():
    phrase = str(input('Como você está se sentindo hoje?: '))
    emotion = analyzer.polarity_scores(phrase)['compound']


    if emotion >= -0.5:
        genre = '18'  # Drama
    elif emotion < 0:
        genre = '35'  # Comédia
    elif emotion < 0.5:
        genre = '10749'  # Romance
    else:
        genre = '27'  # horror

    url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&sort_by=popularity.desc&with_genres={genre}&vote_count.gte=4'
    response = requests.get(url).json()

    if response['results']:
        titles = [result['title'] for result in response['results'][:3]]
        print('Recomendo os seguintes filmes para você:')
        for title in titles:
            print(f' - {title}')
    else:
        print('Não encontrei nenhuma sugestão de filme para você.')

def chatbot():
    print('Olá! Sou um chat de sugestões de filmes. como posso te ajudar hoje?: ')

    while True:
        try:
            response = input('digite filme para sugestões, ou sair para sair: ').lower()
            if 'filme' in response:
                suggest_movies()
            elif 'tchau' in response or 'sair' in response:
                print('Até a próxima!')
                break
            else:
                print('Desculpe, não entendi o que você quis dizer. ')
        except KeyboardInterrupt:
            break
chatbot()