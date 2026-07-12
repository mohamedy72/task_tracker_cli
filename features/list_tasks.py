"""
A module that contains funcionality about listing tasks (all, done, not done, in-progress)
"""


def list_tasks(tasks: list):
    if not tasks:
        print("No tasks found, add new tasks to view them")

    for task in tasks:
        print(f"""
        Task ID: {task["id"]}
        Description: {task["description"]}
        Status: {task["status"]}
        Task Created at: {task["createdAt"]}
        Last Update at: {task["updatedAt"] if task["updatedAt"] else "No modification happened"}
        """)
