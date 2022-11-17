from imdb import downloadFiles,deleteFiles, movies,actors_nums,actors_names
from apiTwitter import tweets
from filesRecording import recording_files
import logging
import os

def create_folders():
    path = os.path.join(os.getcwd(), "imdb", "files")
    if not os.path.exists(path):
        os.makedirs(path)

    path = os.path.join(os.getcwd(), "finalResults")
    if not os.path.exists(path):
        os.makedirs(path)

def log_config():
   path = os.path.join(os.getcwd(), 'finalResults', 'compilado.log')
   logging.basicConfig(filename=path, format='%(asctime)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filemode="w",level=logging.INFO)

def download():
    logging.info("Downloading files!")
    downloadFiles.execute()
    logging.info("Download finished!")

def names_imdb():
    m = movies.get_movies()
    logging.info("First dataset complete!")

    a_nums = actors_nums.get_actors_nums(m)
    logging.info("Second dataset complete!")

    a_names = actors_names.get_actors_names(a_nums)
    logging.info("Third dataset complete!")

    logging.info("Saving names to csv ...")
    recording_files.save_names(a_names)
    logging.info("Names saved in names.csv")

def delete():
    deleteFiles.execute()
    logging.info("Files deleted!")
    
def get_tweets():
    logging.info("Taking actors names ...")
    names = recording_files.get_names()
    logging.info("Actors names found and saved!")

    logging.info("Taking tweets of the actors ...")
    df_tweets = tweets.api_twitter(names)
    logging.info("Tweets found ... ")

    logging.info("Saving tweets to csv ... ")
    recording_files.save_tweets(df_tweets)
    logging.info("Tweets saved in tweets.csv!")

def main():
   create_folders()
   log_config()
   download()
   names_imdb()
   delete()
   get_tweets()

if __name__ == '__main__':
    main()
