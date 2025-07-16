import requests
import sources.newsapi as newsapi

# Stores information about news articles
class NewsArticle:
    def __init__(self,source = None,author = None,title = None,summary = None,imageUrl = None,publishDate = None, content = None):
        self.source = source
        self.author = author
        self.title = title
        self.description = summary
        self.imageUrl = imageUrl
        self.publishDate = publishDate
        self.content = content

def main():
    for article in newsapi.top_articles(country='us',category='technology'):
        print(article.title)

if __name__ == "__main__":
    main()
