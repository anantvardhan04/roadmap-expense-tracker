import json

file_path = "expense_tracker.json"


def write_file(data):
    with open(file_path, "w") as expense_tracker_json:
        json.dump(data, expense_tracker_json, indent=4)


def read_file():
    with open(file_path, "r") as expense_tracker_json:
        data = json.load(expense_tracker_json)
        return data
