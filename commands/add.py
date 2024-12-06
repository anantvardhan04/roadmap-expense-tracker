import os
import json
from .utils import write_file, read_file, file_path


def add_expense(description, amount):
    if not os.path.exists(file_path):
        data = [{"id": 1, "description": description, "amount": f"${amount}"}]
        write_file(data)
        print(f"Expense added successfully (ID: 1)")
    else:
        data = read_file()
        max_id = max((expense_entry["id"] for expense_entry in data)) if data else 0
        next_id = max_id + 1
        expense_entry = {
            "id": next_id,
            "description": description,
            "amount": f"${amount}",
        }
        data.append(expense_entry)
        write_file(data)
        print(f"Expense added successfully (ID: {next_id})")
