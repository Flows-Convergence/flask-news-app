from core import application
from flask import render_template
from .utils import get_latest_news


@application.route('/ast')
def say_hello():
    user = {"name": "Ashutosh"}
    return render_template("index.html", user=user)



@application.route('/')
def news_headlines():
    news_articles = get_latest_news()
    return render_template("news.html", news_articles=news_articles)
