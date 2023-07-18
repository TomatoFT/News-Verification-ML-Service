from fastapi import FastAPI
from inference import *

app = FastAPI()


@app.post("/api/get_news_summarization_content")
def get_news_summarization_content(news_content: str):
    return get_summarization_of_the_news(news_content)
