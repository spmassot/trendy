import config
import feedparser
import logging
import re

from src.google_language import LanguageClient


class Feed:
    proper_noun = re.compile(
        r"\b((?:[A-Z][a-z][-A-Za-z']*(?: *[A-Z][a-z][-A-Za-z']*)*)\b|\b(?:[A-Z][a-z][-A-Za-z']*))"
    )
    html_tag = re.compile(r"<.*?>")
    ignore_topics = (
        'the',
    )

    def __init__(self, url):
        self.url = url
        self.entries = []
        self.topics = []

    def fetch(self):
        try:
            parsed_feed = feedparser.parse(self.url)
            self.entries = parsed_feed.entries
        except Exception as e:
            logging.error(f'failed to fetch {self.url}: {e}')

    def get_topics(self):
        if config.USE_LANGUAGE_API:
            self.topics = self._get_topics_with_language_api()
        else:
            self.topics = self._get_topics_with_regex()
        return self.topics

    def _get_topics_with_language_api(self):
        topics = []
        for entry in self.entries:
            this_entry = f'{entry.title} {entry.description}'
            this_topics = LanguageClient.get_entities(this_entry)
            topics.extend(this_topics)
        return topics
    
    def _get_topics_with_regex(self):
        big_blob = '|'.join([f'{feed.title} {feed.description}' for feed in self.entries])
        big_blob = self.html_tag.sub("", big_blob)
        nouns = self.proper_noun.findall(big_blob)
        topics = {}
        for noun in nouns:
            if noun.lower() in self.ignore_topics:
                continue
            if noun in topics:
                topics[noun] += 1
            else:
                topics[noun] = 1
        return [(k, v) for k, v in topics.items()]
