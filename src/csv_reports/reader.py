import csv
from pathlib import Path

from csv_reports.models import CountryRow


def read_csv_files(file_paths: list[Path]) -> list[CountryRow]:
    """Read multiple CSV files and return a combined list of row dicts."""
    rows: list[CountryRow] = []

    for path in file_paths:
        with open(path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                rows.append(CountryRow.from_dict(row))

    return rows
