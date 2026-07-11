"""
Module to add new tasks
"""
from datetime import datetime

def add_task(new_task: dict, tasks: list):
    # Getting new id
    new_id = len(tasks) + 1
    new_tasks = tasks.append({
        "id": new_id,
        "description": new_task,
        "status": "todo",
        "createdAt": datetime.now(),
        "updatedAt": datetime.now()
    })
    print(f"Task added successfully (ID: {new_id})")
    return new_tasks
