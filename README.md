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
## Delete a Specified Task

**Endpoint:** `DELETE /v1/tasks/{id}`  
**Description:** Delete a task by its ID.

### Response:

- **Status Code:** `204 No Content`
  
#### Body:
No content.
## 5. Edit the Title or Completion of a Specific Task

**Endpoint:** `PUT /v1/tasks/{id}`  
**Description:** Update the title or completion status of a specific task.

### Request Body:
```json
{
  "title": "Updated Task",
  "is_completed": true
}
```
## Bulk Add Multiple Tasks (Extra Credit)

**Endpoint:** `POST /v1/tasks/bulk`  
**Description:** Create multiple tasks in one request.

### Request Body:
```json
{
  "tasks": [
    {"title": "Task 1", "is_completed": false},
    {"title": "Task 2", "is_completed": true}
  ]
}
```
### Response:
```
{
  "tasks": [
    {"id": 1},
    {"id": 2}
  ]
}
```
## Bulk Delete Multiple Tasks (Extra Credit)

**Endpoint:** `DELETE /v1/tasks/bulk`  
**Description:** Delete multiple tasks in one request.

### Request Body:
```json
{
  "tasks": [
    {"id": 1},
    {"id": 2}
  ]
}
```

# How to Run the Server
### Clone the repository to your local machine.

```
git clone https://github.com/anshumanbehera27/WATERDIP-LABS.git
```
### Install the required dependencies:
```
pip install -r requriments.txt
```
### Run the Backend Server 
```
python app.py
```
--
# Testing the Task Tracking Server

This document outlines how to test the API endpoints of the Task Tracking Server. The tests ensure that each endpoint is functioning correctly and returns the expected responses.

## Test Suite Overview

The following test functions are implemented using the `requests` library to interact with the server:

1. **`test_create_task()`**: Tests the creation of a new task.
   - **Checks**:
     - Status code is `201 Created`.
     - The response contains a valid task ID.

2. **`test_list_all_tasks()`**: Tests the retrieval of all tasks.
   - **Checks**:
     - Status code is `200 OK`.
     - The response contains a list of tasks.
     - Each task has valid properties: ID, title, and completion status.

3. **`test_get_task()`**: Tests the retrieval of a specific task by ID.
   - **Checks**:
     - Status code is `200 OK`.
     - The response is a dictionary with valid task properties.

4. **`test_update_task()`**: Tests the update of a specific task's title and completion status.
   - **Checks**:
     - Status code is `204 No Content`.
     - The response contains no content.

5. **`test_delete_task()`**: Tests the deletion of a specific task by ID.
   - **Checks**:
     - Status code is `204 No Content`.
     - The response contains no content.

## Running the Tests

To run the tests, ensure the Task Tracking Server is running locally. Then execute the test script:

```
python test.py
```

