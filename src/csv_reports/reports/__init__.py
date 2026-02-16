from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Any

from csv_reports.models import CountryRow


class Report(ABC):
    @property
    @abstractmethod
    def headers(self) -> list[str]:
        """Column headers for the report."""
        ...

    @abstractmethod
    def generate(self, data: list[CountryRow]) -> list[list[Any]]:
        """Process data and return rows for tabulate output."""
        ...


class ReportRegistry:
    def __init__(self) -> None:
        self._registry: dict[str, type[Report]] = {}

    def register(self, name: str) -> Callable[[type[Report]], type[Report]]:
        """Decorator to register a report class under a given name."""

        def decorator(cls: type[Report]) -> type[Report]:
            self._registry[name] = cls
            return cls

        return decorator

    def get_report(self, name: str) -> Report:
        """Instantiate and return a report by name."""
        if name not in self._registry:
            available = ", ".join(sorted(self._registry))
            raise ValueError(
                f"Unknown report: '{name}'. Available reports: {available}"
            )
        return self._registry[name]()

    def available_reports(self) -> list[str]:
        """Return sorted list of registered report names."""
        return sorted(self._registry)


registry = ReportRegistry()

from csv_reports.reports import average_gdp  # noqa: E402, F401
