from fastapi import FastAPI
from inference import *

app = FastAPI()


@app.post("/api/get_news_categories")
def get_news_categories_content(news_content: str):
    return get_news_categories(news_content)
