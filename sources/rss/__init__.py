import os
import feedparser
from article import NewsArticle

_dirname = os.path.dirname(__file__)
_rss_feeds_path = os.path.join(_dirname, 'rss_feeds.txt')
with open(_rss_feeds_path,"r") as f:
    news_rss_urls = f.readlines()

def articles_from_rss_feed(feed_url):
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        yield _newsarticle_from_rss_entry(entry)

def _newsarticle_from_rss_entry(entry):
    return NewsArticle(
        author      = entry.get("author"),
        title       = entry.get("title"),
        summary     = entry.get("summary"),
        url         = entry.get("link"),
        imageUrl    = entry.get("media_thumbnail"),
        publishDate = entry.get("published"),
    )
