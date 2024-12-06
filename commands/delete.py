from .utils import read_file, write_file


def delete_expense(id: str) -> None:
    data = read_file()
    for expense in data:
        if expense["id"] == id:
            data.remove(expense)
            break

    write_file(data)
    print("Expense deleted successfully")
