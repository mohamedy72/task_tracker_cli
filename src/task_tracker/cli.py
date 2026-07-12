"""
Module contains CLI arguments and optional options
"""
import argparse
from pathlib import Path

from .features.add_task import add_task
from .features.delete_task import delete_task
from .features.list_tasks import list_tasks
from .features.mark_task import change_status
from .features.storage import init_json, load_json, save_json
from .features.update_task import update_task

def main():
    tasks = []
    # Create a new Parser
    parser = argparse.ArgumentParser(prog='tasks-cli', description="CLI tool to manage tasks ( Add, Update, List and Delete tasks) ", epilog="Thanks for using %(prog)s! :)")

    # File to work on, must come before every command/action
    parser.add_argument("--file", default="tasks.json",help="Initialize the JSON storage file")

    ## Add subparser and subcommands
    subparser = parser.add_subparsers(dest="action", title="Actions", help="Actions for various operations on tasks")

    # Add task to a tasks list
    add = subparser.add_parser("add", help="Add new task to a tasks list")
    add.add_argument("task", metavar="task")

    # Update a task by its ID
    update = subparser.add_parser("update", help="Update a task by ID")
    update.add_argument("id", metavar="id_to_update")
    update.add_argument("new_task", metavar="new_task")

    # Delete a task by its ID
    delete = subparser.add_parser("delete", help="Delete a task by ID")
    delete.add_argument("delete_task", metavar="deleted_task")

    # List all tasks
    list = subparser.add_parser("list", help="List all tasks")
    ## Add filters ( todo, done, in-progress )
    list.add_argument("status", nargs="?")

    # TODO: Marking a task as (mark-in-progress | mark-done ) by its ID
    mark_in_progress = subparser.add_parser("mark-in-progress", help="Mark a task as in-progress")
    mark_in_progress.add_argument("id")

    mark_done = subparser.add_parser("mark-done", help="Mark a task as done")
    mark_done.add_argument("id")

    args = parser.parse_args()

    path = Path(args.file).absolute()

    if not path.exists():
        init_json(args.file)
    else:
        tasks = load_json(args.file)

    if args.action == "add":
        add_task(args.task, tasks)
    elif args.action == "update":
        update_task(int(args.id), args.new_task, tasks)
    elif args.action == "delete":
        tasks = delete_task(int(args.delete_task), tasks)
    elif args.action == "list":
        list_tasks(tasks, args.status)
    elif args.action == "mark-in-progress":
        change_status(int(args.id),tasks, "mark-in-progress")
    elif args.action == "mark-done":
        change_status(int(args.id),tasks, "mark-done")


    save_json(path, tasks)
