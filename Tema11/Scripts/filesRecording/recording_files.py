import csv
import pandas as pd 
import os

def save_names(list_names):
    fields = ['nconst', 'qtdMovies','name']
    pathname = os.path.join(os.getcwd(), "finalResults","names.csv")
    with open(pathname, "w",encoding='utf-8') as file:
        w = csv.writer(file)
        w.writerow(fields)
        w.writerows(list_names)

def get_names():
    list_names = []
    pathname = os.path.join(os.getcwd(), "finalResults","names.csv")
    with open(pathname,"r", encoding='utf-8') as file:
        table = csv.DictReader(file)
        for col in table:
            list_names.append(col['name'])
    return list_names

def save_tweets(df_tweets):
    pathname = os.path.join(os.getcwd(), "finalResults","tweets.csv")
    df_tweets.to_csv(pathname,index=False,sep=',')
    '''with open(pathname,"w",encoding="utf-8",newline="") as file:
        #w = csv.DictWriter(file,fieldnames=['Names','Tweets'])
        #w.writeheader()
        for tweet in list_tweets:
            file.write('"{}"\n'.format(tweet))'''






