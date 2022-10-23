import snscrape.modules.twitter as sntwitter
import pandas as pd
import os
from os import environ

limit = environ.get("TWEETS_LIMIT")
delimiter = environ.get("CSV_DELIMITER")


def twitter_scraper(url):

    tweets = []
    print("Iniciando scraper de Twitter")
    for tweet in sntwitter.TwitterSearchScraper(url).get_items():

        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.user.username, tweet.content])

    df = pd.DataFrame(tweets, columns=["Date", "User", "Tweet"])

    # save to csv
    df.to_csv("tweets.csv", sep=delimiter, index=False)
    print('Scraper finalizado')


twitter_scraper("https://twitter.com/IGN/status/1582839867754434562")