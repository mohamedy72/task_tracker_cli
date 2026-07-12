"""
Module contains CLI arguments and optional options
"""
import argparse

def cli():
    # Create a new Parser
    parser = argparse.ArgumentParser(prog='tasks-cli', description="CLI tool to manage tasks ( Add, Update, List and Delete tasks) ", epilog="Thanks for using %(prog)s! :)")

    # File to work on, must come before every command/action
    parser.add_argument("--file", help="Initialize the JSON storage file")

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
    list.add_argument("status")

    # TODO: Marking a task as (mark-in-progress | mark-done ) by its ID
    mark_in_progress = subparser.add_parser("mark-in-progress", help="Mark a task as in-progress")
    mark_in_progress.add_argument("id")

    mark_done = subparser.add_parser("mark-done", help="Mark a task as done")
    mark_done.add_argument("id")

    args = parser.parse_args()

    return args
