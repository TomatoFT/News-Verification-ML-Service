FROM python:3.10.9 as base

ARG DEBIAN_FRONTEND=noninteractive

# Download Poetry
USER root
RUN apt-get install -y curl

# Include poetry into the path
ENV PATH="${PATH}:/root/.local/bin"

# Prevent poetry creating virtual environment before installing depedencies
COPY ./requirements.txt /

# Expose port for the application
EXPOSE 3000

### DEVELOPMENT ###
FROM base as dev

# Install dependencies
# Use a Docker BuildKit cache mountto speed up the installation of Python dependencies
# RUN --mount=type=cache,target=/root/.cache/poetry poetry install

RUN pip install -r requirements.txt
# # Copy application files
COPY . .
# WORKDIR /src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]

# CMD ["python", "inference.py"]

# ### PRODUCTION ###
# FROM base as prod

# # Install dependencies
# # Use a Docker BuildKit cache mountto speed up the installation of Python dependencies
# RUN --mount=type=cache,target=/root/.cache/poetry poetry install

# # Copy application files
# COPY ./src /src
# WORKDIR /src

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
