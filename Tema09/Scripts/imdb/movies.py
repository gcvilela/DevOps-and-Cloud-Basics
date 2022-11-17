import pandas as pd
import os

def get_movies():
    pathname = os.path.join(os.getcwd(), "Scripts", "imdb","files")
    p = os.path.abspath(r'{}/title.basics.tsv'.format(pathname))
    columns = ['tconst','startYear','titleType']
    array_df = []
    for chunk in pd.read_csv(p, sep='\t', chunksize=10000,low_memory=False,usecols=columns):
        temp_df = chunk
        temp_df['startYear'] = temp_df['startYear'].replace(['\\N'], '0')
        temp_df['startYear'] = temp_df['startYear'].astype(int)
        dfMovies = temp_df.loc[(temp_df['titleType'] == 'movie') & (temp_df['startYear'] >= 2012)]
        dfMovies= dfMovies['tconst']
        array_df.append(dfMovies)

    df = pd.concat(array_df, ignore_index=True)

    del temp_df
    del dfMovies

    return df
