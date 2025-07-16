# Stores information about news articles
class NewsArticle:
    def __init__(self, source = None, author = None, title = None, summary = None, url = None, imageUrl = None, publishDate = None, content = None):
        self.source = source
        self.author = author
        self.title = title
        self.summary = summary
        self.url = url
        self.imageUrl = imageUrl
        self.publishDate = publishDate
        self.content = content

    # Convert this article to a pretty, printable string - including all information that is both available and requested
    # 
    # Accepts:
    # - source: whether to include the source, if it is available
    # - author: whether to include the author, if it is available
    # - title: whether to include the title, if it is available
    # - summary: whether to include the summary, if it is available
    # - url: whether to include the url, if it is available
    # - imageUrl: whether to include the imageUrl, if it is available
    # - publishDate: whether to include the publishDate, if it is available
    # - content: whether to include the content, if it is available
    # Returns:
    # - A pretty, printable string including the information requested if it was available
    def to_string(self, source = True, author = True, title = True, summary = True, url = True, imageUrl = False, publishDate = True, content = False):
        # If any of the flags are set to true, attempt to get their corresponding values
        source      = self.source      and source
        author      = self.author      and author
        title       = self.title       and title
        summary     = self.summary     and summary
        url         = self.url         and url
        imageUrl    = self.imageUrl    and imageUrl
        publishDate = self.publishDate and publishDate
        content     = self.content     and content

        # Create the initial string that will be added to
        result = ""
        # First line: {title}
        if title:
            result += title + "\n"
        # Second line: "From {source} ({url})"
        if source:
            result += f"From {source}"
            if url:
                result += f" ({url})"
            result += "\n"
        elif url:
            result += f"From {url}\n"
        # Third line: "Published on {publishDate} by {author}"
        if publishDate or author:
            result += "Published"
            if publishDate:
                result += f" on {publishDate}"
            if author:
                result += f" by {author}"
            result += "\n"
        # Fourth line: "Attached image: {imageUrl}"
        if imageUrl:
            result += f"Attached image: {imageUrl}\n"
        # Fifth line: "Summary: {summary}"
        if summary:
            result += f"Summary: {summary}\n"
        # Sixth line: "Content: {content}"
        if content:
            result += f"Content: {content}\n"
        
        # Return the completed string
        return result
