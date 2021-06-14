import requests
import json
from pathlib import Path
import pandas as pd



def setup_newsapi():
    path = Path.cwd().joinpath("newsapi_cred.json")
    with open(path) as file:
        secrets = json.load(file)

    return secrets





def do_querry(secrets,queryteext,from_published_date='',to_published_date='',page_size=50, page_number=1, auto_correct = True, safe_search= True, with_thumbnails = False):
    
    querystring = {"q": queryteext,
               "pageNumber": page_number,
               "pageSize": page_size, #Max 50 pro Anfrage
               "autoCorrect": auto_correct, #Dass du dich net verschrieben hast
               "safeSearch": safe_search, #wichtig sonst wird es Kriminell
               "withThumbnails": with_thumbnails, #Kostet ne Anfrage --> Besser immer aus lassen
               "fromPublishedDate": from_published_date, 
               "toPublishedDate": to_published_date}
    url = "https://rapidapi.p.rapidapi.com/api/search/NewsSearchAPI"

    response = requests.get(url, headers=secrets, params=querystring).json()

    return response 

def process_response(response):
    dfs = []
    counter = 0
    for page in response['value']:
        counter += 1
        url = page['url']
        title = page['title']
        description = page['description']
        body = page['body']
        date_published = page['datePublished']
        language = page['language']
        inhalt = {'index':counter,'url':url,'title':title,'description':description,'body':body,'date_published':date_published,'language':language}
        dfs.append(inhalt)
    df = pd.DataFrame(dfs)

    return df


