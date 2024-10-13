import requests
import json

def test_create_task():
    try:
        r = requests.post('http://localhost:5000/v1/tasks', json={"title": "Test Task 3"})
        assert r.status_code == 201
        assert isinstance(r.json()["id"], int)
        assert len(r.json()) == 1
        print("test_create_task passed.")
    except Exception as e:
        print(f"test_create_task failed: {e}")

def test_list_all_tasks():
    try:
        r = requests.get('http://localhost:5000/v1/tasks')
        
        assert r.status_code == 200
        assert isinstance(r.json()["tasks"], list)
        assert len(r.json()["tasks"]) > 0
        for task in r.json()["tasks"]:
            assert isinstance(task["id"], int)
            assert isinstance(task["title"], str)
            assert isinstance(task["is_completed"], bool)
            assert len(task) == 3
        print("test_list_all_tasks passed.")
    except Exception as e:
        print(f"test_list_all_tasks failed: {e}")

def test_get_task():
    
    try:
        r = requests.get('http://localhost:5000/v1/tasks/1')
        assert r.status_code == 200
        assert isinstance(r.json(), dict)
        assert isinstance(r.json()["id"], int)
        assert isinstance(r.json()["title"], str)
        assert isinstance(r.json()["is_completed"], bool)
        assert len(r.json()) == 3
        print("test_get_task passed.")
    except Exception as e:
        print(f"test_get_task failed: {e}")

def test_update_task():
    try:
        r = requests.put('http://localhost:5000/v1/tasks/1', json={"title": "My 1st Task", "is_completed": True})
        assert r.status_code == 204
        assert not r.content
        print("test_update_task passed.")
    except Exception as e:
        print(f"test_update_task failed: {e}")

def test_delete_task():
    try:
        r = requests.delete('http://localhost:5000/v1/tasks/1')
        assert r.status_code == 204
        assert not r.content
        print("test_delete_task passed.")
        
    except Exception as e:
        print(f"test_delete_task failed: this is failed  {e}")

if __name__ == '__main__':
    test_create_task()
    test_list_all_tasks()
    test_get_task()
    test_update_task()
    test_delete_task()
    print("All tests executed.")
