# Flask + Redis Docker API

A containerized REST API built with Flask and Redis, orchestrated with Docker Compose.

## What it does
- Tracks visit count persistently using Redis
- Allows storing and retrieving a message via REST endpoints
- Fully containerized, runs with a single command

## Endpoints

GET /
- Returns visit count

POST /message
- saves a message to Redis

GET /message
- retrieves saved message


## Run

git clone https://github.com/SepantaaM/flask-redis-api
cd flask-redis-api
docker compose up --build

## Concepts Demonstrated

- Multi-container orchestration with Docker Compose
- Redis for persistent key-value storage
- RESTful API design with Flask
- Environment variable configuration
