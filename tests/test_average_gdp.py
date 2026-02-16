import pytest

from csv_reports.models import CountryRow
from csv_reports.reports import registry
from csv_reports.reports.average_gdp import AverageGdpReport


def _row(country: str, gdp: str) -> CountryRow:
    return CountryRow(
        country=country,
        year="2023",
        gdp=gdp,
        gdp_growth="0",
        inflation="0",
        unemployment="0",
        population="0",
        continent="X",
    )


class TestAverageGdpReport:
    def setup_method(self) -> None:
        self.report = AverageGdpReport()

    def test_headers(self) -> None:
        result = self.report.headers

        assert result == ["#", "Country", "Average GDP"]

    def test_single_country_single_row(self) -> None:
        data = [_row("A", "100")]

        result = self.report.generate(data)

        assert result == [[1, "A", 100.0]]

    def test_single_country_multiple_rows(self) -> None:
        data = [_row("A", "100"), _row("A", "200"), _row("A", "300")]

        result = self.report.generate(data)

        assert len(result) == 1
        assert result[0][0] == 1
        assert result[0][1] == "A"
        assert result[0][2] == pytest.approx(200.0)

    def test_multiple_countries_sorted_descending(self) -> None:
        data = [_row("Low", "100"), _row("High", "1000"), _row("Mid", "500")]

        result = self.report.generate(data)

        assert [r[1] for r in result] == ["High", "Mid", "Low"]

    def test_average_calculation_across_years(self) -> None:
        data = [
            _row("X", "100"),
            _row("X", "200"),
            _row("Y", "600"),
            _row("Y", "400"),
        ]

        result = self.report.generate(data)

        assert result[0] == [1, "Y", 500.0]
        assert result[1] == [2, "X", 150.0]

    def test_empty_data(self) -> None:
        result = self.report.generate([])

        assert result == []

    def test_registered_in_registry(self) -> None:
        result = registry.get_report("average-gdp")

        assert isinstance(result, AverageGdpReport)


def test_get_report_unknown_raises() -> None:
    with pytest.raises(ValueError, match="Unknown report: 'no-such-report'"):
        registry.get_report("no-such-report")


def test_available_reports_includes_average_gdp() -> None:
    result = registry.available_reports()

    assert "average-gdp" in result
