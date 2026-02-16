from typing import Any

from csv_reports.models import CountryRow
from csv_reports.reports import Report, registry


@registry.register("average-gdp")
class AverageGdpReport(Report):
    """Calculate average GDP per country, sorted by GDP descending."""

    @property
    def headers(self) -> list[str]:
        return ["#", "Country", "Average GDP"]

    def generate(self, data: list[CountryRow]) -> list[list[Any]]:
        gdp_by_country: dict[str, list[float]] = {}

        for row in data:
            country = row.country
            gdp = float(row.gdp)
            gdp_by_country.setdefault(country, []).append(gdp)

        rows: list[list[Any]] = [
            [country, sum(values) / len(values)]
            for country, values in gdp_by_country.items()
        ]
        rows.sort(key=lambda r: r[1], reverse=True)

        return [[i, *row] for i, row in enumerate(rows, start=1)]
