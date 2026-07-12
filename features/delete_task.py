"""
Module to implement task deletion
"""

def delete_task(id: int, tasks: list):
    new_tasks = list(filter(lambda x: x.get("id") != id, tasks))
    print(f"Task with ID {id} is deleted successfully")
    return new_tasks
