"""
Module for marking a task as ( mark-in-progress | mark-dont ) by ID
"""

def change_status(id: int, tasks: list[dict], status: str):
    if not tasks:
        print("Tasks is empty, please add some tasks!")
        return

    for task in tasks:
        if task["id"] == id:
            if status == "mark-in-progress":
                task["status"] = "in-progress"
            else:
                task["status"] =  "done"
            break
