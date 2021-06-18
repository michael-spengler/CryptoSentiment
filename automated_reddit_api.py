subreddits = ['Bitcoin',
'dogecoin',
'CryptoCurrency',
'ethereum',
'ethtrade',
'litecoin',
'btc',
'garlicoin',
'cardano',
'Vechain']

import reddit_crawler
#import twitter_crawler
import time
import pandas as pd


#twitter_api = twitter_crawler.setup_twitter()
reddit_api = reddit_crawler.setup_reddit()

mins = 0

categorie = 'new'  #new, hot, controversial (=heute), top (= müsste all time sein also für uns nutzlos), gilded (auch eher wild wenn man es auf der seite nachschaut)
ex_reddit = reddit_crawler.get_subreddit(reddit_api,subreddits,categorie)
print(type(ex_reddit))

big_df_reddit = pd.DataFrame(columns = ex_reddit.columns)

while True:
    print(f'waiting minute: {mins}')
    time.sleep(120)#sleep for 5 minutes
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
    
    if mins == 60:#zwei stunden sind rum
        break
print('\n\n\n')
print('--- saving data ---')
big_df_reddit.to_csv('18062021_Reddit_CryptoSubreddits120sec_new.csv', sep = ';')