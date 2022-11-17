from imdb import downloadFiles,deleteFiles, movies,actors_nums,actors_names
from apiTwitter import tweets
from filesRecording import recording_files

def download():
    downloadFiles.execute()
    print("Finished")

def names_imdb():
    m = movies.get_movies()
    print("First dataset complete")

    a_nums = actors_nums.get_actors_nums(m)
    print("Second dataset complete")

    a_names = actors_names.get_actors_names(a_nums)
    print("Third dataset complete")

    recording_files.save_names(a_names)

def delete():
    deleteFiles.execute()
    print("Finished")
    
def get_tweets():
    names = recording_files.get_names()
    print("First step complete")
    dfTweets = tweets.api_twitter(names)
    print("Second step complete")
    recording_files.save_tweets(dfTweets)

def main():
   download()
   names_imdb()
   delete()
   get_tweets()

if __name__ == '__main__':
    main()
