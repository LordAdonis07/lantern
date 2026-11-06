import argparse
from storage import load_tasks

parser = argparse.ArgumentParser(prog="lantern")
sub = parser.add_subparsers(dest="command")

add_parser = sub.add_parser("add")
add_parser.add_argument("title")


list_parser = sub.add_parser("list")

list_parser.add_argument(
    "--done",
    action="store_true",
    help="Show only completed tasks"
)

list_parser.add_argument(
    "--sort",
    action="store_true",
    help="Sort tasks alphabetically by title"
)

args = parser.parse_args()

if args.command == "add":
    print("add:", args.title)


elif args.command == "list":
    tasks = load_tasks()

    if args.done:
        tasks = [task for task in tasks if task.get("done", False)]

    if not tasks:
        print("No tasks found.")
    else:
        if args.sort:
            tasks = sorted(
                tasks,
                key=lambda task: task["title"].casefold()
            )

        for task in tasks:
            print(task["title"])

