# from load_to_hdfs import append_data_to_hdfs_file, read_hdfs_data_file, create_the_hdfs_file
import json

from fastapi import FastAPI
from kafka_server import get_data_from_consumer, push_data_to_producer
from load_to_mysql_db import load_the_data_to_db, observe_the_data_from_table
from newspaper import Article

app = FastAPI()


@app.post("/api/get_news_content_from_user")
def get_news_content_from_url(news_url: str, is_verified: bool):
    article = Article(news_url, language="vi")
    article.download()
    article.parse()
    results = {
        "Source": news_url.split("/")[2],
        "Title": article.title,
        "Content": article.text,
        "Is_verified": is_verified,
    }

    serialized_value = json.dumps(results).encode("utf-8")
    push_data_to_producer(serialized_value)

    msg = get_data_from_consumer()
    decode_value = ""
    if msg == None:
        print("ERROR")
    else:
        decode_value = msg.value().decode("utf-8")
        load_the_data_to_db(decode_value)
        print("INSERT TO KAFKA SUCCESSFULLY")
    observe_the_data_from_table()

    return results
