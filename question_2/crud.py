# CRUD Operations
from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

# Database connection function
def get_db():
    return mysql.connector.connect(
        host="localhost", user="root", password="password", database="task_manager_db"
    )

# Task model
class Task(BaseModel):
    title: str
    description: str
    due_date: str

# CRUD Operations (defined as functions here)
def create_task(task: Task):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO tasks (title, description, due_date) VALUES (%s, %s, %s)", 
                   (task.title, task.description, task.due_date))
    db.commit()
    cursor.close()
    db.close()

def get_tasks():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    db.close()
    return tasks

def update_task(task_id: int, task: Task):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "UPDATE tasks SET title = %s, description = %s, due_date = %s WHERE task_id = %s",
        (task.title, task.description, task.due_date, task_id),
    )
    db.commit()
    cursor.close()
    db.close()

def delete_task(task_id: int):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM tasks WHERE task_id = %s", (task_id,))
    db.commit()
    cursor.close()
    db.close()

