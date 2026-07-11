"""
Module to implement task deletion
"""

def delete_task(id: int, tasks: list):
    for task in tasks:
        if task["id"] == id:
            del task
    return f"Task with ID {id} is deleted successfully"
