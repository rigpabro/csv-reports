from pathlib import Path

import pytest

from csv_reports.cli import parse_args


def test_parse_valid_args(sample_csv: Path) -> None:
    result = parse_args(["--files", str(sample_csv), "--report", "average-gdp"])

    assert result.files == [sample_csv]
    assert result.report == "average-gdp"


def test_parse_multiple_files(sample_csv: Path, sample_csv_2: Path) -> None:
    result = parse_args([
        "--files",
        str(sample_csv),
        str(sample_csv_2),
        "--report",
        "average-gdp",
    ])

    assert len(result.files) == 2


def test_missing_files_arg(sample_csv: Path) -> None:
    with pytest.raises(SystemExit):
        parse_args(["--report", "average-gdp"])


def test_missing_report_arg(sample_csv: Path) -> None:
    with pytest.raises(SystemExit):
        parse_args(["--files", str(sample_csv)])


def test_invalid_report_name(sample_csv: Path) -> None:
    with pytest.raises(SystemExit):
        parse_args(["--files", str(sample_csv), "--report", "nonexistent"])


def test_nonexistent_file() -> None:
    with pytest.raises(SystemExit):
        parse_args(["--files", "/no/such/file.csv", "--report", "average-gdp"])
