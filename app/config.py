import os


FEED_URLS = (
    "http://rss.cnn.com/rss/cnn_topstories.rss",
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "http://feeds.foxnews.com/foxnews/latest",
)
USE_LANGUAGE_API = os.getenv('USE_LANGUAGE_API') == 'true'
