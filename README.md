# Full JWT Server with Django and Docker

## Overview

This repository contains a Django-based server implementation with full JWT (JSON Web Token) authentication. It is designed to be run in a Docker environment, providing scalability and ease of deployment.

## Features

- JWT-based authentication
- Django REST Framework for API development
- Dockerized for easy deployment
- Scalable and modular codebase

## Requirements

- Docker installed on your system
- Basic understanding of Django and JWT

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/full-jwt-server.git
    ```

2. Navigate to the project directory:

    ```bash
    cd full-jwt-server
    ```

3. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

4. Access the server at [http://localhost:8000](http://localhost:8000)

## API Endpoints

- **Register User:**

  `POST /api/register/`

  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
