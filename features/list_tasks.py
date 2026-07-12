"""
A module that contains funcionality about listing tasks (all, done, not done, in-progress)
"""


def list_tasks(tasks: list, status: str):
    if not tasks:
        print("No tasks found, add new tasks to view them")

    tasks_to_print = []
    if status:
        tasks_to_print = list(filter(lambda item: item["status"] == status, tasks))
    else:
        tasks_to_print = tasks

    for task in tasks_to_print:
            print(f"""
            Task ID: {task["id"]}
            Description: {task["description"]}
            Status: {task["status"]}
            Task Created at: {task["createdAt"]}
            Last Update at: {task["updatedAt"] if task["updatedAt"] else "No modification happened"}
            """)
