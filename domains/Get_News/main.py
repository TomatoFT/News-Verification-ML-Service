# from load_to_hdfs import append_data_to_hdfs_file, read_hdfs_data_file, create_the_hdfs_file
import json

import requests
from fastapi import FastAPI
from kafka_server import OnlineKafkaServer

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
print(server.get_consumer(name="consumer-1").name)
consumer = server.get_consumer(name="consumer-1")

server.create_producer(name="producer-1")
producer = server.get_producer(name="producer-1")
print(producer)

app = FastAPI()


# @app.post("/news/feature_extraction")
def get_news_content_from_url(news_url: str, is_verified: bool):
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

    # results["Summarization"] = get_summarization_of_the_news(results["Content"])
    # results["Categories"] = get_news_categories(results["Content"])

    serialized_value = json.dumps(results).encode("utf-8")
    producer.push_data(topic=topic, value=serialized_value)

    msg = consumer.consumer.poll(1.0)
    print("msg", msg)
    decode_value = ""
    if msg == None:
        print("ERROR")
    else:
        decode_value = msg.value().decode("utf-8")
        decoded_dict = json.loads(decode_value)
        print(decoded_dict)
        # load_the_data_to_db(results)
        print("INSERT TO KAFKA SUCCESSFULLY")
    # observe_the_data_from_table()

    return results


results = get_news_content_from_url(
    news_url="https://thanhnien.vn/bo-cong-an-bat-dong-san-nhat-nam-da-lua-dao-huy-dong-gan-9000-ti-dong-185230930182113574.htm",
    is_verified=True,
)

print(results)
