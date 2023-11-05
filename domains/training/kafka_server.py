# import json
import random
import string

from confluent_kafka import Consumer, Producer

class OnlineKafkaServer:
    # Kafka broker configuration
    def __init__(self, bootstrap_servers, topic, group_id):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.group_id = group_id

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