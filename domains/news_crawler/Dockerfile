# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy your source code to the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install pandas

# Expose the Airflow ports
EXPOSE 8081 5555 8793

# Install Airflow
RUN pip install apache-airflow

# Initialize the Airflow database
RUN airflow db init

# Set up Airflow environment variables
ENV AIRFLOW_HOME=/app/airflow

# Copy the DAG file to the Airflow DAGs directory
COPY ./dag.py /app/airflow/dags/

# Start Airflow web server and scheduler
CMD ["airflow", "webserver", "--port", "8081"]
