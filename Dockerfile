FROM apache/airflow:2.6.3
RUN pip install --user --upgrade pip
RUN pip install newspaper3k
RUN pip install confluent_kafka