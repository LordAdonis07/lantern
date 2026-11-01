import argparse

parser = argparse.ArgumentParser(prog="lantern")
sub = parser.add_subparsers(dest="command")

add_parser = sub.add_parser("add")
add_parser.add_argument("title")
list_parser = sub.add_parser("list")

args = parser.parse_args()

if args.command == "add":
    print("add:", args.title)
elif args.command == "list":
    print("list")
