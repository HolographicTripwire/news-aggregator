import requests
import sources.newsapi as newsapi
import sources.rss as rss
from sources import no_repeats, round_robin

def main():
    newsapi_sources = [
        newsapi.top_articles(country='us'),
        newsapi.top_articles(country='gb'),
    ]
    rss_sources = [rss.articles_from_rss_feed(url) for url in rss.news_rss_urls]
    sources = newsapi_sources + rss_sources
    for article in no_repeats(round_robin(sources)):
        print(article.to_string() + "\n")

if __name__ == "__main__":
    main()
