import pandas as pd


def get_actors_names(actors):
    df = pd.read_csv(r"C:\Users\Mariana Moreira\PycharmProjects\Tema06\venv\Scripts\imdb\files\name.basics.tsv",sep='\t', low_memory=False)
    dfNames =  pd.merge(actors, df, on="nconst")
    dfTopActors = dfNames[['nconst', 'qtdMovies', 'primaryName']]
    dfTopActors = dfTopActors.head(10)
    lista = dfTopActors.values.tolist()
    return lista