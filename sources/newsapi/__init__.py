import os
import requests
from article import NewsArticle

# The url for newsapi
_top_headlines_url = "https://newsapi.org/v2/top-headlines"
# Get the api key
_dirname = os.path.dirname(__file__)
_api_key_path = os.path.join(_dirname, 'api_key.txt')
with open(_api_key_path,"r") as f:
    _api_key = f.read()

# Get all news articles from newsapi with the provided parameters
# 
# Accepts:
# - **parameters: the parameters to pass into newsApi
# Returns:
# - A generator of NewsArticle objects from newsapi matching the provided parameters
# Raises:
# - Exception containing error message if the request doesn't return a successful 200 status
def top_articles(**parameters):
    # Get our api key and add it to the parameters 
    with open(_api_key_path,"r") as f:
        parameters["apiKey"] = f.read()
    # Get a data from newsapi
    response = requests.get(_top_headlines_url, params=parameters)
    data = response.json()
    # Yield all articles if there are no errors
    if data['status'] == 'ok':
        for article in data['articles']:
            yield _newsarticle_from_newsapi_article(article)
    # Otherwise raise an exception specifying the error
    else:
        raise Exception(f"Error: {data['message']}")

# Convert a newsapi article to a NewsArticle object
# 
# Accepts:
# - article; the article to be converted, in dictionary form exactly as it was fetched from newsapi
# Returns:
# - A NewsArticle object containing all the details from the provided newsapi article
def _newsarticle_from_newsapi_article(article):
    return NewsArticle(
        source      = article["source"],
        author      = article["author"],
        title       = article["title"],
        summary     = article["description"],
        imageUrl    = article["urlToImage"],
        publishDate = article["publishedAt"],
        content     = article["content"]
    )
