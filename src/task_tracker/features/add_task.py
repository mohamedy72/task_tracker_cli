"""
Module to add new tasks
"""
from datetime import datetime

def add_task(new_task: dict, tasks: list):
    # Getting new id
    new_id = len(tasks) + 1
    tasks.append({
        "id": new_id,
        "description": new_task,
        "status": "todo",
        "createdAt": str(datetime.now()),
        "updatedAt": str(datetime.now())
    })
    print(f"Task added successfully (ID: {new_id})")
