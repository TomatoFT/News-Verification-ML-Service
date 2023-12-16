from typing import Any
from newspaper import Article

class GetArticle:
    def __init__(self, url) -> None:
        self.url = url
        self.article = Article(url)
    
    def __call__(self) -> Any:
        self.article.download()
        self.article.parse()
        return self

    def url(self):
        return self.url
    
    def get_title(self):
        return self.article.title
    
    def get_authors(self):
        return self.article.authors
    
    def get_publish_date(self):
        return self.article.publish_date
    
    def get_content(self):
        return self.article.text