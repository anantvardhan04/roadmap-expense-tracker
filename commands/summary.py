from .utils import read_file


def summarize_expense() -> float:
    total_expense = 0
    data = read_file()
    if data:
        for record in data:
            total_expense += float(record["amount"])
    else:
        print("No expense records found!")
    return total_expense

