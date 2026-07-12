from pathlib import Path
from features.delete_task import delete_task
from features.list_tasks import list_tasks
from layers.cli import cli
from features.storage import init_json, load_json, save_json
from features.add_task import add_task
from features.update_task import update_task

def main():
    tasks = []
    args = cli()
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
        list_tasks(tasks)

    save_json(path, tasks)

if __name__ == "__main__":
    main()
