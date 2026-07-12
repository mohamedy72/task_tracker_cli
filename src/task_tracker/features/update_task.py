"""
Module to update a task using its ID
"""
from datetime import datetime

def update_task(id: int, new_task: str, tasks: list):
    if not tasks:
        raise ValueError("Task list is empty. Cannot update")

    for task in tasks:
        if task["id"] == id:
            task["description"] = new_task
            task["updatedAt"] = str(datetime.now())
            return f"Task with ID {id} updated successfully"
