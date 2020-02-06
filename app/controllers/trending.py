import config
import json
import src.feeds as feeds

from flask import Blueprint


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
