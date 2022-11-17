from logs import twitterLogs
from datetime import datetime
import tweepy as tw
import pandas as pd
import dotenv
import os
import re

def get_tokens():
    dotenv.load_dotenv(dotenv.find_dotenv())
    consumer_key= os.getenv("API_KEY")
    consumer_secret = os.getenv("API_KEY_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    #bearer_token = os.getenv("BEARER_TOKEN")
    return consumer_key,consumer_secret,access_token,access_token_secret

def clean_tweet(tweets_text):
    clean_text = re.sub(r'RT+', '', tweets_text)
    clean_text = clean_text.replace("\n", " ")
    clean_text = clean_text.replace(",", " ")
    clean_text = clean_text.replace('"', " ")

    return clean_text

def get_api():
    consumer_key, consumer_secret, access_token, access_token_secret = get_tokens()
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    return api

def api_twitter(list_names):
    api = get_api()
    list_tweets = []
    total_results = 0
    for n in list_names:
        name = n.replace(" ", "")
        count_results = 0
        query = '{}'.format(name)
        result = api.search_tweets(q=query,count = 100)
        if (not (result is None)):
            for tweet in result:
                text = clean_tweet(tweet.text)
                date = format(tweet.created_at,"%Y-%m-%d")
                list_tweets.append([name,tweet.id,text,date,tweet.user.name])
                count_results += 1

        twitterLogs.log(name, count_results)
        total_results += count_results

    df = pd.DataFrame(list_tweets,columns=['Name','Tweet Id','Tweet Text','Date','User'])
    twitterLogs.total(total_results)
    return df





