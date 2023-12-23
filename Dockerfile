
# Assuming AIRFLOW_UID and AIRFLOW_GID are environment variables
ARG AIRFLOW_UID=50000
ARG AIRFLOW_GID=0
ARG AIRFLOW_PROJ_DIR='./domains/news_crawler'

FROM apache/airflow:2.1.2

USER root
RUN groupadd --gid ${AIRFLOW_GID} airflow && \
    useradd --uid ${AIRFLOW_UID} --gid ${AIRFLOW_GID} --create-home --shell /bin/bash --home /home/airflow airflow

RUN pip install --user --upgrade pip
RUN pip install newspaper3k
RUN pip install confluent_kafka


USER airflow
