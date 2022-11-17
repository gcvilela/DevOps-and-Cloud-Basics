from imdb import movies, actors_nums, actors_names
from apiTwitter import tweets
from filesRecording import recording_files

def path(file_name):
    p = r"path\Scripts\imdb\files\{}".format(file_name)
    return p

def names_imdb():
    p = path("title.basics.tsv")
    m = movies.get_movies(p)
    p = path("title.principals.tsv")
    a_nums = actors_nums.get_actors_nums(p,m)
    p = path("name.basics.tsv")
    a_names = actors_names.get_actors_names(p,a_nums)
    recording_files.save_names(a_names)

def get_tweets():
    names = recording_files.get_names()
    dfTweets = tweets.api_twitter(names)
    recording_files.save_tweets(dfTweets)

def main():
   names_imdb()
   get_tweets()

if __name__ == '__main__':
    main()
