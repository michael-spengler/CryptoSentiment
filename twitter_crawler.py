import tweepy as tw
from pathlib import Path
import json
import pandas as pd

def setup_twitter():
    path = Path.cwd().joinpath("twitter_cred.json")
    with open(path) as file:
        secrets = json.load(file)
  
    

    auth = tw.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
    auth.set_access_token(secrets['access_token_key'], secrets['access_token_secret'])

    twitter_api = tw.API(auth)

    return twitter_api


def searchword(twitter_api, search_words, date_since,num_items):
    tweets = tw.Cursor(twitter_api.search,
              q=search_words,
              lang="en",
              since=date_since).items(num_items)


    dfs = []
    counter = 0
    for tweet in tweets:
        print(tweet)
        created = tweet.created_at
        text = tweet.text
        language = tweet.metadata['iso_language_code']
        likes = tweet.favorite_count
        inhalt = {'index':counter,'body':text,'date_published':created,'likes':likes,'language':language}
        dfs.append(inhalt)
    df = pd.DataFrame(dfs)
    return df


def find_user_timeline(twitter_api,id,count):
    tweets = twitter_api.user_timeline(id=id,since_id=None,max_id=None,count=count)
    
    dfs = []
    counter = 0
    for tweet in tweets:
        created = tweet.created_at
        text = tweet.text
        likes = tweet.favorite_count
        inhalt = {'index':counter,'body':text,'date_published':created,'likes':likes}
        dfs.append(inhalt)
    df = pd.DataFrame(dfs)
    return df



