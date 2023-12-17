from typing import Any

from newspaper import Article, ArticleException


class GetArticle:
    def __init__(self, url) -> None:
        self.url = url
        self.article = Article(url)
        self.title = None
        self.authors = None
        self.publish_date = None
        self.content = None
    
    def __call__(self) -> Any:
        try:
            self.article.download()
            self.article.parse()
            self.title = self.article.title
            self.authors = self.article.authors
            self.publish_date = self.article.publish_date
            self.content = self.article.text
        except ArticleException as e:
            print(f"Error processing URL {self.url}: {e}")

        return self

    def get_title(self):
        return self.title
    
    def get_authors(self):
        return self.authors
    
    def get_publish_date(self):
        return self.publish_date
    
    def get_content(self):
        return self.content
