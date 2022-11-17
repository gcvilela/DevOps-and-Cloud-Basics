import pandas as pd

def get_movies():
    df = pd.read_csv(r"C:\Users\Mariana Moreira\PycharmProjects\Tema06\venv\Scripts\imdb\files\title.basics.tsv", sep='\t', low_memory=False)
    df['startYear'] = df['startYear'].replace(['\\N'],'0')
    df['startYear'] = df['startYear'].astype(int)
    dfMovies = df.loc[(df['titleType'] == 'movie') & (df['startYear'] >= 2012)]
    dfTitulos = dfMovies['tconst']

    return dfTitulos