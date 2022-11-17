import csv
import pandas as pd 
import os

def save_names(list_names):
    fields = ['nconst', 'qtdMovies','name']
    pathname = os.path.join(os.getcwd(), "finalResults")
    with open(r"{}/names.csv".format(pathname), "w",encoding='utf-8') as file:
        w = csv.writer(file)
        w.writerow(fields)
        w.writerows(list_names)

def get_names():
    list_names = []
    pathname = os.path.join(os.getcwd(), "finalResults")
    with open(r"{}/names.csv".format(pathname),"r", encoding='utf-8') as file:
        table = csv.DictReader(file)
        for col in table:
            list_names.append(col['name'])
    return list_names

def save_tweets(dfTweets):
    pathname = os.path.join(os.getcwd(), "finalResults")
    dfTweets.to_csv(r"{}/tweets.csv".format(pathname),index=False,sep='\t')
    del dfTweets
