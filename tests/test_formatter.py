import pytest

from csv_reports.formatter import print_report


def test_print_report(capsys: pytest.CaptureFixture[str]) -> None:
    headers = ["Name", "Value"]
    rows = [["Alpha", 100], ["Beta", 200]]
    print_report(headers, rows)

    result = capsys.readouterr()

    assert "Alpha" in result.out
    assert "Beta" in result.out
    assert "100" in result.out
    assert "200" in result.out


def test_print_report_empty(capsys: pytest.CaptureFixture[str]) -> None:
    print_report(["Name", "Value"], [])

    result = capsys.readouterr()

    assert "Name" in result.out
    assert "Value" in result.out
