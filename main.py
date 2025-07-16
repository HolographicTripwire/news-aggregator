import requests
import sources.newsapi as newsapi

def main():
    for article in newsapi.top_articles(country='us',category='technology'):
        print(article.title)

if __name__ == "__main__":
    main()
