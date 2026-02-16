from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CountryRow:
    country: str
    year: str
    gdp: str
    gdp_growth: str
    inflation: str
    unemployment: str
    population: str
    continent: str

    @classmethod
    def from_dict(cls, raw: dict[str, str]) -> CountryRow:
        return cls(
            country=raw["country"],
            year=raw["year"],
            gdp=raw["gdp"],
            gdp_growth=raw["gdp_growth"],
            inflation=raw["inflation"],
            unemployment=raw["unemployment"],
            population=raw["population"],
            continent=raw["continent"],
        )
