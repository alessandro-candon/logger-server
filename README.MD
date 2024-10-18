# FastAPI Uvicorn Web Service with Docker

This project provides a simple web service built with FastAPI and Uvicorn, 
running in a Docker container. 
Its primary purpose is to log every incoming request for testing, debugging, or monitoring purposes.

## Purpose

- **Request Logging:** This tool logs every HTTP request received by the server, including details such as the HTTP method, request URL, headers, query parameters, and response status code.
- **Testing:** Ideal for developers who need a lightweight, customizable web service to test client applications, HTTP requests, or API integrations.
- **Debugging:** Useful for debugging issues with requests or identifying unexpected patterns in client-server interactions.
- **Monitoring:** Can be employed as a simple monitoring tool to observe incoming traffic in real-time.

## Features

- Supports all HTTP methods: GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD
- Handles any path and logs all request details
- Dockerized setup using Docker and Docker Compose for easy deployment

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup

1. Clone the repository or create the following files in a new directory
2. Run `docker-compose up` to build and start the container
3. Access the web service at `http://localhost:8099` and see all requests logged in the terminal
