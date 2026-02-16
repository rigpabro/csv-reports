from pathlib import Path

from csv_reports.reader import read_csv_files


def test_read_single_file(sample_csv: Path) -> None:
    result = read_csv_files([sample_csv])

    assert len(result) == 4
    assert result[0].country == "CountryA"
    assert result[0].gdp == "1000"


def test_read_multiple_files(sample_csv: Path, sample_csv_2: Path) -> None:
    result = read_csv_files([sample_csv, sample_csv_2])

    assert len(result) == 6
    countries = {row.country for row in result}
    assert countries == {"CountryA", "CountryB", "CountryC"}


def test_read_preserves_all_columns(sample_csv: Path) -> None:
    expected_fields = {
        "country",
        "year",
        "gdp",
        "gdp_growth",
        "inflation",
        "unemployment",
        "population",
        "continent",
    }

    result = read_csv_files([sample_csv])

    assert set(vars(result[0]).keys()) == expected_fields


def test_read_empty_list() -> None:
    result = read_csv_files([])

    assert result == []
