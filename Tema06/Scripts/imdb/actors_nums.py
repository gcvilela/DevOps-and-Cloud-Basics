import pandas as pd

def get_actors_nums(movies):
    df = pd.read_csv(r"C:\Users\Mariana Moreira\PycharmProjects\Tema06\venv\Scripts\imdb\files\title.principals.tsv",
                     sep='\t', low_memory=False)
    dfActors = df.loc[(df['category'] == 'actor') | (df['category'] == 'actress')]
    dfMerge = pd.merge(movies, dfActors, on="tconst")

    dfTopTen = dfMerge['nconst'].value_counts()
    dfTopTen = dfTopTen.reset_index()
    dfTopTen.rename(columns={'nconst': 'qtdMovies'}, inplace=True)
    dfTopTen.rename(columns={'index': 'nconst'}, inplace=True)

    return dfTopTen