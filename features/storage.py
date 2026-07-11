"""
A module that contains storage functionality ( init, save and load ) using JSON file
"""

import json
from pathlib import Path

# Init our tasks JSON file
def init_json(filename: str):
    path = Path(filename).absolute()
    if path.suffix != ".json":
         raise ValueError("File name must be a json file")

    with open(filename, "w") as f:
        json.dump([], f)
        print("File successfully created!")

# Load from json
def load_json(filename: str)-> list:
    path = Path(filename).absolute()

    if path.suffix != ".json":
         raise ValueError("File name must be a json file")

    if not path.exists():
        raise FileNotFoundError("File not found. Please run `task-cli init`")

    with open(filename, "r") as f:
        tasks = json.load(f)

    return tasks

# Save to json
def save_json(filename, data):
    path = Path(filename).absolute()

    if path.suffix != ".json":
        raise ValueError("File name must be a json file")

    if not path.exists():
        raise FileNotFoundError("File not found. Please check any typos or run `task-cli init`")

    ## If filename exists
    ### Load already existing data
    tasks: list = load_json(filename)
    new_tasks = tasks.append(data)
    with open(filename, "w") as f:
        json.dump(new_tasks, f)
