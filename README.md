# Task Tracking Server

## Overview

This project is a simple task tracking server built using Flask and SQLite. It allows users to manage tasks with various features, including creating, listing, retrieving, updating, and deleting tasks. The server also supports bulk operations for adding and deleting multiple tasks in one request.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **SQLite**: A self-contained, serverless, zero-configuration, transactional SQL database engine.
- **Pydantic**: For data validation and settings management using Python type annotations.

## API Endpoints

The server exposes the following API endpoints:

### 1. Create a New Task

- **Endpoint**: `POST /v1/tasks`
- **Description**: Create a new task with a title and completion status.
- **Request Body**:
  ```json
  {
    "title": "My Task",
    "is_completed": false
  }

- **Response Body**:
```json

    {
  "id": 1
}
```
## 2. List All Tasks

**Endpoint:** `GET /v1/tasks`  
**Description:** Retrieve a list of all tasks.

### Response:

- **Status Code:** `200 OK`
  
#### Body:
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "My Task",
      "is_completed": false
    }
  ]
}
```
## 3. Get a Specific Task

**Endpoint:** `GET /v1/tasks/{id}`  
**Description:** Retrieve details of a specific task by its ID.

### Response:

- **Status Code:** `200 OK`
  
#### Body:
```json
{
  "id": 1,
  "title": "My Task",
  "is_completed": false
}
```
