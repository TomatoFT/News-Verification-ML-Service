FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-devel as base

ARG DEBIAN_FRONTEND=noninteractive

# Download Poetry
RUN apt-get update && apt-get install -y curl git
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN mkdir /app/ /var/logs/

COPY ./pyproject.toml poetry.lock /

# Include poetry into the path
ENV PATH="${PATH}:/root/.local/bin"

# Prevent poetry creating virtual environment before installing depedencies
RUN poetry config virtualenvs.create false

# Expose port for the application
EXPOSE 3000

### DEVELOPMENT ###
FROM base as dev

# Install dependencies
# Use a Docker BuildKit cache mountto speed up the installation of Python dependencies
# RUN --mount=type=cache,target=/root/.cache/poetry poetry install

RUN poetry install
# # Copy application files
COPY . .
# WORKDIR /src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]

# ### PRODUCTION ###
# FROM base as prod

# # Install dependencies
# # Use a Docker BuildKit cache mountto speed up the installation of Python dependencies
# RUN --mount=type=cache,target=/root/.cache/poetry poetry install

# # Copy application files
# COPY ./src /src
# WORKDIR /src

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
