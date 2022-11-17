import pandas as pd

def get_actors_nums(p,movies):
    columns = ['tconst', 'category', 'nconst']
    array_df = []
    for chunk in pd.read_csv(p, sep='\t', chunksize=100000, low_memory=False,usecols=columns):
       temp_df = chunk
       dfActors = temp_df.loc[(temp_df['category'] == 'actor') | (temp_df['category'] == 'actress')]
       dfActors = pd.merge(movies, dfActors, on="tconst")
       array_df.append(dfActors)

    df = pd.concat(array_df, ignore_index=True)
    dfTopTen = df['nconst'].value_counts()
    dfTopTen = dfTopTen.reset_index()
    dfTopTen.rename(columns={'nconst': 'qtdMovies'}, inplace=True)
    dfTopTen.rename(columns={'index': 'nconst'}, inplace=True)


    del temp_df
    del dfActors
    del df

    return dfTopTen
