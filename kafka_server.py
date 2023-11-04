# import json
import random
import string

from confluent_kafka import Consumer, Producer

# Kafka broker configuration
bootstrap_servers = "kafka:9092"
topic = "uit-news-verifcation"


def generate_the_keys():
    return "".join(random.choices(string.ascii_lowercase, k=4))


producer = Producer({"bootstrap.servers": bootstrap_servers})
consumer = Consumer(
    {
        "bootstrap.servers": bootstrap_servers,
        "group.id": "my-group",
        "auto.offset.reset": "earliest",
    }
)

# Create Kafka producer
def push_data_to_producer(value, key=generate_the_keys()):
    # Produce a message to Kafka
    producer.produce(topic, key=key, value=value)
    producer.flush()

# Create Kafka consumer
def get_data_from_consumer():
    consumer.subscribe([topic])
    msg = consumer.poll(1.0)
    return msg
