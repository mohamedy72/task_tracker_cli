"""
Module contains CLI arguments and optional options
"""
import argparse


def cli():
    # Create a new Parser
    parser = argparse.ArgumentParser(prog='tasks-cli', description="CLI tool to manage tasks ( Add, Update, List and Delete tasks) ", epilog="Thanks for using %(prog)s! :)")

    # Add task argument group
    add = parser.add_argument_group("Add tasks commands:")
    add.add_argument("add")

    # Update and Delete argument group
    modifying = parser.add_argument_group("Updating and Deleting by ID commands:")
    modifying.add_argument("update")
    modifying.add_argument("delete")

    # List tasks argument group
    listing = parser.add_argument_group("Listing all and by status commands:")
    ## List all for now
    listing.add_argument("list")
    ## TODO: List by status

    # Marking tasks argument group. Subcommands for List
    ## TODO

    args = parser.parse_args()

    return args
