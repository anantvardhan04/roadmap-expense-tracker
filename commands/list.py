from .utils import read_file
from tabulate import tabulate


def list_expense() -> None:
    data = read_file()  # list of dictionaries
    print(tabulate(data, headers="keys", tablefmt="pretty"))
