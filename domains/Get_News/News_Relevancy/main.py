from fastapi import FastAPI
from inference import *

app = FastAPI()


@app.post("/api/get_the_revelancy_score")
def get_the_revelancy_score(first_news_content: str, seconnd_news_content: str):
    score = get_the_similarity_score(first_news_content, seconnd_news_content)
    return {"score": score}
