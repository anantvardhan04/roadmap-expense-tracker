from .utils import read_file, write_file


def update_expense(id: int, description: str, amount: str) -> None:
    # 1. Read the file and load the data in a variable
    data = read_file()
    # 2. Do a for loop through expense records, and if a match of id is found, update the fields.
    if data:
        for record in data:
            if record["id"] == id:
                record["description"] = description
                record["amount"] = f"${amount}"
                break
    else:
        print("No expense records found to update")
        return

    # 3. Write the data back to the file
    write_file(data)
    print(f"Expense updated successfully (ID: {id})")
