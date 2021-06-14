import praw
import json
from pathlib import Path
import pandas as pd

def setup_reddit():
    path = Path.cwd().joinpath("reddit_cred.json")
    with open(path) as file:
        secrets = json.load(file)

    reddit = praw.Reddit(client_id = secrets["client_id"], client_secret = secrets["client_secret"], 
        user_agent = secrets["user_agent"], username = secrets["username"], password = secrets["password"])

    reddit.read_only
    return reddit

def get_subreddit(reddit,subreddits,categorie,limit=1000):
    submissions = []

    if categorie == 'hot':
        for subreddit in subreddits:
            for submission in reddit.subreddit(subreddit).hot(limit=limit):
                submissions.append([submission.title, submission.score,submission.id,submission.subreddit,
                submission.num_comments,submission.selftext, submission.created])

    if categorie == 'new':
        for subreddit in subreddits:
            for submission in reddit.subreddit(subreddit).new(limit=limit):
                submissions.append([submission.title, submission.score,submission.id,submission.subreddit,
                submission.num_comments,submission.selftext, submission.created])

    if categorie == 'controversial':
        for subreddit in subreddits:
            for submission in reddit.subreddit(subreddit).controversial(limit=limit):
                submissions.append([submission.title, submission.score,submission.id,submission.subreddit,
                submission.num_comments,submission.selftext, submission.created])

    if categorie == 'top':
        for subreddit in subreddits:
            for submission in reddit.subreddit(subreddit).top(limit=limit):
                submissions.append([submission.title, submission.score,submission.id,submission.subreddit,
                submission.num_comments,submission.selftext, submission.created])

    if categorie == 'gilded':
        for subreddit in subreddits:
            for submission in reddit.subreddit(subreddit).gilded(limit=limit):
                submissions.append([submission.title, submission.score,submission.id,submission.subreddit,
                submission.num_comments,submission.selftext, submission.created])


    submission = pd.DataFrame(submissions,columns=['title', 'score', 'id', 'subreddit', 'num_comments', 'body', 'created'])
    return submission

def find_subreddits(reddit,keyword):
    subreddits = []
    for subreddit in reddit.subreddits.search_by_name(keyword):
        subreddits.append(str(subreddit))
    return subreddits

