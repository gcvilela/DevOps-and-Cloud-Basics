import tweepy as tw
import pandas as pd
import dotenv
import os

def get_token():
    dotenv.load_dotenv(dotenv.find_dotenv())
    bearer_token = os.getenv("BEARER_TOKEN")
    return bearer_token

def api_twitter(list_names):
    bt = get_token()
    client = tw.Client(bearer_token=bt)
    tweet_dic = {}
    for n in list_names:
        name = n.replace(" ","")
        list_tweets = []
        query = '#{} -is:retweet'.format(name)
        print(query)
        result = client.search_recent_tweets(query=query,max_results = 10)
        if(not(result.data is None)):
            for tweet in result.data:
                list_tweets.append(tweet.text)
        tweet_dic[name] = list_tweets

    df = pd.DataFrame.from_dict(tweet_dic,orient='index')
    df = df.T.melt().dropna()
    df = df.rename(columns={'variable':'name','value':'tweet'})
    df = df.explode('tweet')
    
    return df



