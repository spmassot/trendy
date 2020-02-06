import json
from datetime import datetime
from flask import Blueprint

import config
import src.google_language as lang
import src.feeds as feeds


routes = Blueprint('trending', __name__)


@routes.route('/trending')
def trending():
    topics = []
    for url in config.FEED_URLS:
        feed = feeds.Feed(url)
        feed.fetch()
        topics.extend(feed.get_topics())
    sorted_topics = sorted(topics, key=lambda x: x[1], reverse=True)
    return json.dumps({'topics': [t[0] for t in sorted_topics[:5]]})
