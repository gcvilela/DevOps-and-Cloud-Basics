import csv
import pandas as pd 

def save_names(list_names):
    fields = ['nconst', 'qtdMovies','name']
    with open(r"path\Scripts\finalResults\names.csv", "w",encoding='utf-8') as file:
        w = csv.writer(file)
        w.writerow(fields)
        w.writerows(list_names)

def get_names():
    list_names = []
    with open(r"path\Scripts\finalResults\names.csv","r", encoding='utf-8') as file:
        table = csv.DictReader(file)
        for col in table:
            list_names.append(col['name'])
    return list_names

def save_tweets(dfTweets):
    dfTweets.to_csv(r"path\Scripts\finalResults\tweets.csv",index=False,sep='\t')
    del dfTweets
