import requests
import json

def test_create_task():
    try:
        r = requests.post('http://localhost:5000/v1/tasks', json={"title": "Test Task 3"})
        assert r.status_code == 201  # Check for status code 201 (Created)
        assert isinstance(r.json()["id"], int)  # Ensure ID is an integer
        assert len(r.json()) == 1  # Ensure only one key in response
        print("test_create_task passed.")
    except Exception as e:
        print(f"test_create_task failed: {e}")

def test_list_all_tasks():
    try:
        r = requests.get('http://localhost:5000/v1/tasks')
        assert r.status_code == 200  # Check for status code 200 (OK)
        assert isinstance(r.json()["tasks"], list)  # Ensure tasks is a list
        assert len(r.json()["tasks"]) > 0  # Ensure the list is not empty
        for task in r.json()["tasks"]:
            assert isinstance(task["id"], int)  # Ensure ID is an integer
            assert isinstance(task["title"], str)  # Ensure title is a string
            assert isinstance(task["is_completed"], bool)  # Ensure is_completed is a boolean
            assert len(task) == 3  # Ensure each task has 3 keys
        print("test_list_all_tasks passed.")
    except Exception as e:
        print(f"test_list_all_tasks failed: {e}")

def test_get_task():
    try:
        r = requests.get('http://localhost:5000/v1/tasks/1')
        assert r.status_code == 200  # Check for status code 200 (OK)
        assert isinstance(r.json(), dict)  # Ensure the response is a dictionary
        assert isinstance(r.json()["id"], int)  # Ensure ID is an integer
        assert isinstance(r.json()["title"], str)  # Ensure title is a string
        assert isinstance(r.json()["is_completed"], bool)  # Ensure is_completed is a boolean
        assert len(r.json()) == 3  # Ensure the task has 3 keys
        print("test_get_task passed.")
    except Exception as e:
        print(f"test_get_task failed: {e}")

def test_update_task():
    try:
        r = requests.put('http://localhost:5000/v1/tasks/1', json={"title": "My 1st Task", "is_completed": True})
        assert r.status_code == 204  # Check for status code 204 (No Content)
        assert not r.content  # Ensure response content is empty
        print("test_update_task passed.")
    except Exception as e:
        print(f"test_update_task failed: {e}")

def test_delete_task():
    try:
        r = requests.delete('http://localhost:5000/v1/tasks/1')
        assert r.status_code == 204  # Check for status code 204 (No Content)
        assert not r.content  # Ensure response content is empty
        print("test_delete_task passed.")
    except Exception as e:
        print(f"test_delete_task failed: {e}")

# Add a function to run all tests when this file is executed
if __name__ == '__main__':
    test_create_task()
    test_list_all_tasks()
    test_get_task()
    test_update_task()
    test_delete_task()
    print("All tests executed.")
