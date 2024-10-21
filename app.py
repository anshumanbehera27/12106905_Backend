import logging
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel, ValidationError, Field
from typing import List, Optional
from contextlib import contextmanager

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

# Models
class TaskModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)

# Pydantic Schemas
class TaskCreateSchema(BaseModel):
    title: str = Field(..., max_length=100, description="The title of the task")
    is_completed: Optional[bool] = Field(default=False, description="Completion status of the task")

class TaskListSchema(BaseModel):
    id: int
    title: str
    is_completed: bool

    class Config:
        from_attributes = True

# Create the database
with app.app_context():
    db.create_all()

@contextmanager
def session_scope():
    session = db.session
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def api_response(data=None, error=None, status=200):
    response = {"data": data, "error": error}
    return jsonify(response), status

@app.route('/')
def hello():
    return jsonify("Welcome to The Task Api")
    


# Create new task
@app.route('/v1/tasks', methods=['POST'])
def create_task():
    try:
        # get JSON data 
        data = request.get_json()
        task_schema = TaskCreateSchema(**data)  

        # Create a new TaskModel instance
        new_task = TaskModel(title=task_schema.title, is_completed=task_schema.is_completed)

        # Add the new task to the database
        db.session.add(new_task)
        db.session.commit()

        # Return the ID of the newly created task
        return jsonify({'id': new_task.id}), 201

    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get all tasks
@app.route('/v1/tasks', methods=['GET'])
def list_tasks():
    try:
        tasks = TaskModel.query.all()  # Query all tasks from the database
        return jsonify({'tasks': [TaskListSchema.from_orm(task).dict() for task in tasks]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get a specific task by ID
@app.route('/v1/tasks/<int:id>', methods=['GET'])
def get_task(id):
    try:
        task = TaskModel.query.get(id)

        if task is None:
            return jsonify({'error': 'There is no task at that id'}), 404

        return jsonify(TaskListSchema.from_orm(task).dict()), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to delete a specific task
@app.route('/v1/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    try:
        task = TaskModel.query.get(id)

        if task is None:
            return jsonify({'error': 'There is no task at that id'}), 404

        db.session.delete(task)
        db.session.commit()

        return '', 204

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to update a specific task
@app.route('/v1/tasks/<int:id>', methods=['PUT'])
def edit_task(id):
    try:
        task = TaskModel.query.get(id)

        if task is None:
            return jsonify({'error': 'There is no task at that id'}), 404

        data = request.get_json()

        if 'title' in data:
            task.title = data['title']  # Update title
        if 'is_completed' in data:
            task.is_completed = data['is_completed']  # Update completion status

        db.session.commit()

        return '', 204

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to bulk create tasks
@app.route('/v1/tasks/bulk', methods=['POST'])
def bulk_create_tasks():
    try:
        data = request.get_json()

        if 'tasks' not in data:
            return jsonify({'error': 'Missing tasks key in the request body'}), 400

        tasks = data['tasks']
        new_tasks = []

        for task_data in tasks:
            task_schema = TaskCreateSchema(**task_data)  # Validate using Pydantic
            new_task = TaskModel(title=task_schema.title, is_completed=task_schema.is_completed)
            new_tasks.append(new_task)

        db.session.bulk_save_objects(new_tasks)
        db.session.commit()

        return jsonify({'tasks': [{'id': task.id} for task in new_tasks]}), 201

    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Endpoint to bulk delete tasks
@app.route('/v1/tasks/bulk', methods=['DELETE'])
def bulk_delete_tasks():
    try:
        data = request.get_json()

        if 'tasks' not in data:
            return jsonify({'error': 'Missing tasks key in the request body'}), 400

        tasks = data['tasks']
        missing_ids = []

        for task_data in tasks:
            task_id = task_data.get('id')
            if TaskModel.query.get(task_id) is None:
                missing_ids.append(task_id)

        if missing_ids:
            return jsonify({'error': f'Task IDs not found: {missing_ids}'}), 404

        for task_data in tasks:
            task_id = task_data['id']
            task = TaskModel.query.get(task_id)
            db.session.delete(task)

        db.session.commit()
        return '', 204

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
