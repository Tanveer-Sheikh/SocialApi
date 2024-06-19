# SocialApi
API for social networking application using Django Rest Framework


### Complete README.md

```markdown
# SocialApi

API for a social networking application using Django Rest Framework.

## Django Friend Request API

This is a Django application for managing user registrations, logins, and friend requests.

## Project Overview

This project provides a simple API for handling user sign-ups, logins, and friend request functionalities. Users can send, accept, reject, and view friend requests. Additionally, they can search for other users and see a list of their friends.

### Features

- User Registration
- User Login
- Send Friend Request
- Accept Friend Request
- Reject Friend Request
- List Friends
- Search Users
- View Pending Friend Requests

## Installation

### Clone the Repository

```sh
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### Setting Up the Environment

1. **Create a virtual environment and activate it:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the database migrations:**
    ```sh
    python manage.py migrate
    ```

4. **Create a superuser (optional but recommended):**
    ```sh
    python manage.py createsuperuser
    ```

5. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## Docker Setup

To run the application with Docker:

1. **Build the Docker image:**
    ```sh
    docker-compose build
    ```

2. **Run the Docker container:**
    ```sh
    docker-compose up
    ```

### Docker Compose and Dockerfile

#### Dockerfile

```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Django app
EXPOSE 8000

# Run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

#### docker-compose.yml

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - DEBUG=1
```


## Postman Collection API Endpoints

### User Registration

- **URL**: `/signup/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "email": "user@example.com",
      "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
      "data": "User Created"
  }
  ```

### User Login

- **URL**: `/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "email": "user@example.com",
      "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
      "data": "Login success",
      "csrf_token": "csrf_token"
  }
  ```

### Send Friend Request

- **URL**: `/SendRequest/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "username": "friend_username"
  }
  ```
- **Response**:
  ```json
  {
      "data": "Request Send"
  }
  ```

### Reject Friend Request

- **URL**: `/RejectRequest/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "username": "friend_username"
  }
  ```
- **Response**:
  ```json
  {
      "data": "Request Rejected"
  }
  ```

### Accept Friend Request

- **URL**: `/AcceptRequest/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "username": "friend_username"
  }
  ```
- **Response**:
  ```json
  {
      "data": "Request Accepted"
  }
  ```

### List of Friends

- **URL**: `/ListOfFriends/`
- **Method**: `GET`
- **Response**:
  ```json
  {
      "data": ["friend1", "friend2"]
  }
  ```

### Search Users

- **URL**: `/SearchUsers/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "keyword": "search_keyword",
      "page_no": 1
  }
  ```
- **Response**:
  ```json
  {
      "data": ["user1", "user2"]
  }
  ```

### Pending Friend Requests

- **URL**: `/PendingRequests/`
- **Method**: `GET`
- **Response**:
  ```json
  {
      "data": ["pending_user1", "pending_user2"]
  }
  ```

## Requirements

- Python 3.x
- Django 3.x
- Django Rest Framework
- Docker
- Docker Compose


