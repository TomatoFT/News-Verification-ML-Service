# import json
import random
import string

from confluent_kafka import Consumer, Producer


def generate_the_keys():
    return "".join(random.choices(string.ascii_lowercase, k=4))


class KafkaConsumer:
    def __init__(self, name, bootstrap_servers, group_id) -> None:
        self.consumer = Consumer(
            {
                "bootstrap.servers": bootstrap_servers,
                "group.id": group_id,
                "auto.offset.reset": "earliest",
            }
        )
        self.name = name

    def subscribe(self, topic):
        self.consumer.subscribe([topic])


class KafkaProducer:
    def __init__(self, bootstrap_servers, name) -> None:
        self.producer = Producer({"bootstrap.servers": bootstrap_servers})
        self.name = name

    def push_data(self, topic, value, key=generate_the_keys()):
        # Produce a message to Kafka
        self.producer.produce(topic, key=key, value=value)
        self.producer.flush()


class KafkaTopic:
    def __init__(self) -> None:
        self.topics = []

    @classmethod
    def add_topic(self, topic):
        self.topics.append(topic)

    @classmethod
    def remove_topic(self, topic):
        if topic in self.topics:
            self.topics.remove(topic)


class OnlineKafkaServer:
    def __init__(self, bootstrap_servers: str, group_id: str):
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        self.consumer_list = []
        self.producer_list = []

    def create_consumer(self, name: str, topic: KafkaTopic):
        consumer = KafkaConsumer(
            name=name, bootstrap_servers=self.bootstrap_servers, group_id=self.group_id
        )
        consumer.subscribe(topic)
        self.consumer_list.append(consumer)

    def create_producer(self, name: str):
        # Create a Kafka producer
        producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers, name=name)
        self.producer_list.append(producer)

    def get_consumer(self, name: str):
        for consumer in self.consumer_list:
            if consumer.name == name:
                return consumer.consumer
        return "Consumer not existed"

    def get_producer(self, name: str):
        for producer in self.producer_list:
            if producer.name == name:
                return producer.producer
        return "Producer not existed"
