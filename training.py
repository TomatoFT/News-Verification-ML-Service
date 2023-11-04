from confluent_kafka import Producer
from models.GRU import training
from kafka_server import get_data_from_consumer, push_data_to_producer
import logging

logger = logging.getLogger(__name__)
# Set up Kafka producer
# producer = Producer({'bootstrap.servers': 'kafka:9092'})

# Serialize the training function
# def train_model(data):
#     # Training logic here
#     pass

serialized_function = str(training)

# Create a Kafka topic
# topic = 'training_topic'

# Send the function to Kafka
# producer.produce(topic, value=serialized_function)
# producer.flush()
push_data_to_producer(value=serialized_function)

logger.info(get_data_from_consumer())