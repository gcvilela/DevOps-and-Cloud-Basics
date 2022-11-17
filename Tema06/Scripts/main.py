from imdb import movies, actors_nums, actors_names
from dbConnection import mysql_connection
from apiTwitter import tweets

def names_imdb(connect):
    m = movies.get_movies()
    a_nums = actors_nums.get_actors_nums(m)
    a_names = actors_names.get_actors_names(a_nums)
    connect.insert_names(a_names)

def get_tweets(connect):
    names = connect.get_names()
    print(names)
    tweets_dic = tweets.api_twitter(names)

    for actor,tweet in tweets_dic.items():
        print('='*50)
        print("Name:",actor,"\nTweets:")
        print('-'*50)
        for i in tweet:
            print(i)
            print('-'*50)

def main():
   connect = mysql_connection.connector_mysql()
   names_imdb(connect)
   get_tweets(connect)

if __name__ == '__main__':
    main()


