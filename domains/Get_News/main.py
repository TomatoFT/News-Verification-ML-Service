# from load_to_hdfs import append_data_to_hdfs_file, read_hdfs_data_file, create_the_hdfs_file
import json
import time

import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from kafka_server import OnlineKafkaServer, generate_the_keys
# from load_to_mysql_db import load_the_data_to_db, observe_the_data_from_table
# from News_Classification.inference import (
#     get_entities_of_news,
#     get_news_categories,
#     get_sentiment_of_the_news,
# )
# from News_Summarization.inference import get_summarization_of_the_news
from newspaper import Article

# Kafka broker configuration
bootstrap_servers = "kafka:9092"

topic = "task_topic"
group_id = "training_test_1"

# create Kafka server
server = OnlineKafkaServer(bootstrap_servers=bootstrap_servers, group_id=group_id)

server.create_consumer(name="consumer-1", topic=topic)
print(server.get_consumer(name="consumer-1").consumer)
consumer = server.get_consumer(name="consumer-1").consumer

server.create_producer(name="producer-1")
producer = server.get_producer(name="producer-1").producer
print(producer)

app = FastAPI()


origins = ["*"]  # Allow all origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


@app.post("/news/collect")
def get_news_content_from_url(news_url: str, is_verified: bool):
    print('enter the function')

    article = Article(news_url, language="vi")
    article.download()
    article.parse()
    results = {
        "Source": news_url.split("/")[2],
        "Title": article.title,
        "Content": article.text,
        "Is_verified": str(is_verified),
    }
    # Add the summarize_content
    print("Crawl successfully")
    # results["Summarization"] = get_summarization_of_the_news(results["Content"])
    # results["Categories"] = get_news_categories(results["Content"])

    serialized_value = json.dumps(results).encode("utf-8")
    # producer.push_data(topic=topic, value=serialized_value)
    producer.produce(topic=topic, key=generate_the_keys(), value=serialized_value)
    producer.flush()
    print('Add the data successfully')


    # msg = consumer.poll(1.0)
    # print("msg", msg)
    # decode_value = ""
    # if msg == None:
    #     print("ERROR")
    # else:
    #     decode_value = msg.value().decode("utf-8")
    #     decoded_dict = json.loads(decode_value)
    #     print(decoded_dict)
    #     # load_the_data_to_db(results)
    #     print("INSERT TO KAFKA SUCCESSFULLY")
    # # observe_the_data_from_table()

    return results

