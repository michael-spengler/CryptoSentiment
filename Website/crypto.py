from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import pandas as pd 
import reddit_crawler
import twitter_crawler
import newsapi_crawler

twitter_api = twitter_crawler.setup_twitter()
reddit_api = reddit_crawler.setup_reddit()
newsapi_api = newsapi_crawler.setup_newsapi()

app = Flask(__name__)

@app.route("/")
def index():
    engines = [['Choose Search Engine'], ['Twitter'], ['Reddit'], ['News']]
    reddit_cats = [['new'], ['hot'], ['controversial'], ['top'], ['gilded']]

    return render_template("base.html", engines=engines, reddit_cats=reddit_cats)


@app.route("/results", methods=['POST', 'GET'])
def results():
    print('args:', request.args)
    print('form:', request.form)
    suche = request.args.get("engine")
    #suche = request.form.get("engine")
    print(suche)

    return render_template("results.html", suche=suche)

# Impressum erstellen!
@app.route("/about")
def imp():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug = True)