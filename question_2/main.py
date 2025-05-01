from fastapi import FastAPI
from crud import create_task, get_tasks, update_task, delete_task
from pydantic import BaseModel

app = FastAPI()

# Task model
class Task(BaseModel):
    title: str
    description: str
    due_date: str

# Routes (imported from `crud.py`)
@app.post("/tasks/")
def create_task_route(task: Task):
    create_task(task)  # Calls the function from `crud.py`
    return {"message": "Task created successfully"}

@app.get("/tasks/")
def get_tasks_route():
    tasks = get_tasks()  # Calls the function from `crud.py`
    return {"tasks": tasks}

@app.put("/tasks/{task_id}")
def update_task_route(task_id: int, task: Task):
    update_task(task_id, task)  # Calls the function from `crud.py`
    return {"message": "Task updated successfully"}

@app.delete("/tasks/{task_id}")
def delete_task_route(task_id: int):
    delete_task(task_id)  # Calls the function from `crud.py`
    return {"message": "Task deleted successfully"}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API!"}


