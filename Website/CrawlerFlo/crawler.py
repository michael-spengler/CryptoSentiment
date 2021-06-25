import pandas as pd 
import reddit_crawler
import twitter_crawler
import newsapi_crawler

"""
Authentifizierung vornehmen
--> Um direkt direkt beim Start der Anwendung das gemacht zu machen
"""

#RECHT WEIT NACH OBEN KLATSCHEN
twitter_api = twitter_crawler.setup_twitter()
reddit_api = reddit_crawler.setup_reddit()
newsapi_api = newsapi_crawler.setup_newsapi()


"""
Newsapi: Anfragen tätigen
--> in: newsapi_api, querytext
   --> optional: page_number, page_size, auto_correct, safe_search, with_thumbnails, from_published_date, to_published_date
--> out: Dataframe mit: index, url, title, description, body, date_published, language 

Anmerkung:
- Maximale page_size: 50
- safe_search Search besser immer True/nichts eintragen
- with_thumbnails besser immer False, sonst 2 API-Anfragen
"""

####1 INPUT FELD FÜR TEXT##########

#querytext = 'bitcoin' #DEIN INPUT SEIN
#response = newsapi_crawler.do_querry(newsapi_api,querytext,page_size=1)
#df =  newsapi_crawler.process_response(response)



""""
Redditapi Subreddits zu einem Namen finden
--> in: reddit_crawler, searchword
--> out: subreddits (Liste mit allen Reddits die den Suchtext im Namen haben)
"""

####FINDE PASSENDE SUBREDDITS ZU DEINEM THEMA
#1 INPUT FELD

#subreddits_string = 'bitcoin'
#subreddits = reddit_crawler.find_subreddits(reddit_api,subreddits_string)
#print(subreddits)

"""
Redditapi Reddits abfragen
--> in: subreddits (Liste), categorie, limit
   --> zusätzlich: limit 
--> out: df mit: title, score, id, subreddit, num_comments, body, created

Anmerkung:
Limit gibt an wie Nachrichten maximal empfangen werden können, ggf. sind es auch weniger
Categories

"""


####FINDE PASSENDE NACHRICHTEN AUS DEINEM SUBREDDIT
#1 INPUT FELD

#####EVTL RADIOBUTTONS
#subreddits = ['Bitcoin','BitcoinBeginners']
#categorie = 'new'  #new, hot, controversial (=heute), top (= müsste all time sein also für uns nutzlos), gilded (auch eher wild wenn man es auf der seite nachschaut)
#df = reddit_crawler.get_subreddit(reddit_api,subreddits,categorie)
#print(df)

"""
TwitterAPI nach einem Wort suchen
--> in: twitter_api, search_words,date_since, num_items
--> out:df mit index, body, date_published, likes, language

Anmerkung:
- date_since funktioniert eher mäßig
"""



####FINDE PASSENDE TWEETS ZU DEM THEMA
#1 INPUT FELD

#search_words = 'bitcoin'
#date_since = '2021-05-20' 
#num_items  = 10
#df = twitter_crawler.searchword(twitter_api, search_words, date_since,num_items)


"""
TwitterAPI nach einem Wort suchen
--> in: twitter_api, search_words,date_since, num_items
--> out:df mit index, body, date_published, likes, language

Anmerkung:
- Datum funktioniert nicht
"""


####FINDE PASSENDE TWEETS ZU DEINEN PERSONEN
#1 INPUT FELD

#id='@elonmusk'
#num_items = 10
#df = twitter_crawler.find_user_timeline(twitter_api,id,num_items)
#print(df)


