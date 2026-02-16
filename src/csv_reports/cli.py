import argparse
from pathlib import Path

from csv_reports.reports import registry


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse and validate command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate reports from macroeconomic CSV data."
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        type=Path,
        help="Paths to CSV data files.",
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=registry.available_reports(),
        help="Name of the report to generate.",
    )

    args = parser.parse_args(argv)

    for path in args.files:
        if not path.is_file():
            parser.error(f"File not found: {path}")

    return args
