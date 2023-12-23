# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files to the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Set up cron job
RUN chmod +x /app/cron.sh
RUN crontab /app/cron.sh

CMD ["cron", "-f"]
