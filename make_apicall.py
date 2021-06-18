import pandas as pd 

import reddit_crawler
import twitter_crawler
import newsapi_crawler

import time

twitter_api = twitter_crawler.setup_twitter()
reddit_api = reddit_crawler.setup_reddit()

mins = 0

#ex_reddit = reddit_crawler.find_subreddits(reddit_api,'bitcoin')
subreddits = ['bitcoin']#,'blockchain']
categorie = 'new'  #new, hot, controversial (=heute), top (= müsste all time sein also für uns nutzlos), gilded (auch eher wild wenn man es auf der seite nachschaut)
ex_reddit = reddit_crawler.get_subreddit(reddit_api,subreddits,categorie)
print(type(ex_reddit))


search_words = 'bitcoin'
num_items  = 1
date_since = '2021-05-20' 
ex_twitter = twitter_crawler.searchword(twitter_api, date_since = date_since,search_words = search_words,num_items = num_items)
print(type(ex_twitter))


big_df_reddit = pd.DataFrame(columns = ex_reddit.columns)
big_df_twitter = pd.DataFrame(columns = ex_twitter.columns)

while True:
    print(f'waiting minute: {mins}')
    time.sleep(300)#sleep for 5 minutes
    mins += 1

    #api_call hier
    try:
        reddit_ = reddit_crawler.get_subreddit(reddit_api,subreddits,categorie)
        big_df_reddit = big_df_reddit.append(reddit_)
        print('\n\n\n')
        print('reddit dataframe updated')
    except Exception as e:
        print('_______ REDDIT ERROR ________')
        print(e)
    try:
        num_items  = 100
        twitter_ = twitter_crawler.searchword(twitter_api, date_since = date_since,search_words = search_words,num_items = num_items)
        big_df_twitter = big_df_twitter.append(twitter_)
        print('twitter dataframe updated')
    except Exception as e:
        print('_______ TWITTER ERROR ________')
        print(e)
    
    if mins == 24:#zwei stunden sind rum
        break
print('\n\n\n')
print('--- saving data ---')
big_df_reddit.to_csv('18062021_Reddit_Bitcoin_new.csv', sep = ';')
big_df_twitter.to_csv('18062021_Twitter_Bitcoin.csv', sep = ';')