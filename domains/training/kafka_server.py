# import json
import random
import string

from confluent_kafka import Consumer, Producer

class KafkaConsumer:
    def __init__(self, name, bootstrap_servers, group_id) -> None:
        self.consumer = Consumer({
            'bootstrap.servers': bootstrap_servers,
            'group.id': group_id,
            'auto.offset.reset': 'earliest'
        })
        self.name = name

class KafkaProducer:
    def __init__(self, bootstrap_servers, name) -> None:
        self.producer = Producer({'bootstrap.servers': bootstrap_servers})
        self.name = name


class OnlineKafkaServer:
    def __init__(self, bootstrap_servers, topic, group_id):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.group_id = group_id
        self.consumer_list = []
        self.producer_list = []

    def create_consumer(self):
        self.consumer = Consumer({
            'bootstrap.servers': self.bootstrap_servers,
            'group.id': self.group_id,
            'auto.offset.reset': 'earliest'
        })
        # Subscribe to the topic
        self.consumer.subscribe([self.topic])
        return self.consumer

    def create_producer(self):
        # Create a Kafka producer
        self.producer = Producer({'bootstrap.servers': self.bootstrap_servers})
        return self.producer