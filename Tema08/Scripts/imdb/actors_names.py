import pandas as pd

def get_actors_names(p,actors):
    columns = ['nconst','primaryName']
    array_df = []
    for chunk in pd.read_csv(p, sep='\t', chunksize=10000, low_memory=False, usecols=columns):
        temp_df = chunk
        df = pd.merge(actors, temp_df, on="nconst")
        array_df.append(df)

    df = pd.concat(array_df, ignore_index=True)
    dfTopActors = df[['nconst', 'qtdMovies', 'primaryName']]
    dfTopActors = dfTopActors.sort_values(by=['qtdMovies'], ascending=False)
    dfTopActors = dfTopActors.head(10)
    list_names = dfTopActors.values.tolist()

    del df
    del dfTopActors

    return list_names
