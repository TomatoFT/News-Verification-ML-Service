import time

from confluent_kafka import Consumer, KafkaException, Producer

from models import CNN_GRU, CNN_LSTM, GRU, LSTM, Transformer
from kafka_server import OnlineKafkaServer

# Kafka broker configuration
bootstrap_servers = 'kafka:9092'
topic = 'task_topic'
group_id = 'training_test_1'

# create Kafka server
online_learning_server = OnlineKafkaServer(bootstrap_servers=bootstrap_servers,
                                           topic=topic,
                                           group_id=group_id)

producer = online_learning_server.create_producer()
consumer = online_learning_server.create_consumer()

# Forever loop
while True:
    # Task details
    task = "Retrain model"

    # Produce the task message
    producer.produce(topic, value=str(task).encode('utf-8'))

    # Flush the producer to ensure the message is sent
    producer.flush()

    # Wait for 20 seconds before sending the next task
    time.sleep(20)

    # Consume messages
    try:
        msg = consumer.poll(1.0)
        print(msg)
        if msg is None:
            continue

        if msg.error():
            if msg.error().code() == KafkaException.PARTITION_EOF:
                # End of partition event
                print(f'Reached end of partition {msg.partition()}')
            else:
                # Error
                print(f'Error occurred: {msg.error().str()}')
            continue

        # Process the message
        task = msg.value().decode('utf-8')
        print(task)
        if task == "Retrain model":
            GRU.training()
            LSTM.training()
            CNN_LSTM.training()
            CNN_GRU.training()
            Transformer.training()
        else:
            print('Task not Found')

    except KeyboardInterrupt:
        break

# Close the consumer and producer
consumer.close()
producer.flush()
producer.close()