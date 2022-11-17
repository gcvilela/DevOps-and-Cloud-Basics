import logging
import os

def log(actor,num):
    path = os.path.join(os.getcwd(),'finalResults','tweets.log')
    logging.basicConfig(filename=path,format='%(asctime)s : %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p',filemode="w",level=logging.INFO)

    logging.info("Actor query: %s",actor)
    logging.info('Number of tweets: %s',num)


def total(total_results):
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    logging.info('Total tweets: %s',total_results)