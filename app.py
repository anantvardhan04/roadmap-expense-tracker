import argparse
from commands.add import add_expense
from commands.list import list_expense
from commands.update import update_expense
from commands.delete import delete_expense
from commands.summary import summarize_expense


def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command")

    add_subparser = subparser.add_parser("add", help="Add expenses")
    add_subparser.add_argument(
        "--description", type=str, help="Add the description for the expense"
    )
    add_subparser.add_argument(
        "--amount", type=str, help="Add the expense amount", required=True
    )

    # Update subparser
    # expense-tracker update <id> --description <value> --amount <value>
    update_subparser = subparser.add_parser("update", help="Update the expense record")
    update_subparser.add_argument(
        "id", type=int, help="Provide the expense ID to be updated"
    )
    update_subparser.add_argument(
        "--description", type=str, help="Provide the expense description", required=True
    )
    update_subparser.add_argument(
        "--amount", type=str, help="Provide the expense amount", required=True
    )

    # List subparser
    list_subparser = subparser.add_parser("list", help="list all expenses")

    # Delete subparser
    # expense-tracker delete --id <id>
    delete_subparser = subparser.add_parser("delete", help="Delete the expense record")
    delete_subparser.add_argument(
        "--id", type=int, help="Provide the expense ID to be deleted"
    )

    # Summary subparser
    summary_subparser = subparser.add_parser(
        "summary", help="Give the total of all expenses"
    )

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "list":
        list_expense()
    elif args.command == "update":
        update_expense(args.id, args.description, args.amount)
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "summary":
        total_expense = summarize_expense()
        print(f"Total expense is: {total_expense}")


if __name__ == "__main__":
    main()
