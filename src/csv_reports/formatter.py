from typing import Any

from tabulate import tabulate


def print_report(headers: list[str], rows: list[list[Any]]) -> None:
    """Print a formatted table to stdout."""
    print(tabulate(rows, headers=headers, tablefmt="grid"))
