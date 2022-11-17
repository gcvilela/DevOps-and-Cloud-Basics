import tweepy as tw
import pandas as pd
from .tokens import BEARER_TOKEN 

def api_twitter(lista):
    cliente = tw.Client(bearer_token=BEARER_TOKEN)
    tweet_dic = {}
    for name in lista:
        list = []
        nome = name.replace(" ","")
        query = '#{} -is:retweet'.format(nome)
        print(query)
        result = cliente.search_recent_tweets(query=query,max_results = 10)
        if(not(result.data is None)):
            for tweet in result.data:
                list.append(tweet.text)
        tweet_dic[nome] = list

    return tweet_dic
