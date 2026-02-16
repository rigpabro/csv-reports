import subprocess
import sys
from pathlib import Path

import pytest


def run_script(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "csv_reports", *args],
        capture_output=True,
        text=True,
    )


class TestIntegration:
    def test_average_gdp_single_file(self, sample_csv: Path) -> None:
        result = run_script("--files", str(sample_csv), "--report", "average-gdp")

        assert result.returncode == 0
        assert "CountryA" in result.stdout
        assert "CountryB" in result.stdout

    def test_average_gdp_multiple_files(
        self, sample_csv: Path, sample_csv_2: Path
    ) -> None:
        result = run_script(
            "--files",
            str(sample_csv),
            str(sample_csv_2),
            "--report",
            "average-gdp",
        )

        assert result.returncode == 0
        assert "CountryA" in result.stdout
        assert "CountryB" in result.stdout
        assert "CountryC" in result.stdout

    def test_output_sorted_descending(
        self, sample_csv: Path, sample_csv_2: Path
    ) -> None:
        result = run_script(
            "--files",
            str(sample_csv),
            str(sample_csv_2),
            "--report",
            "average-gdp",
        )

        lines = result.stdout.strip().split("\n")
        # CountryC (2000) should appear before CountryA (900) before CountryB (450)
        country_order = [
            line.split("|")[2].strip()
            for line in lines
            if "|" in line and "Average GDP" not in line and "=" not in line
        ]
        assert country_order == ["CountryC", "CountryA", "CountryB"]

    def test_invalid_report_exits_with_error(self, sample_csv: Path) -> None:
        result = run_script("--files", str(sample_csv), "--report", "bad-report")

        assert result.returncode != 0

    def test_no_args_exits_with_error(self) -> None:
        result = run_script()

        assert result.returncode != 0

    def test_nonexistent_file_exits_with_error(self) -> None:
        result = run_script(
            "--files", "/no/such/file.csv", "--report", "average-gdp"
        )

        assert result.returncode != 0

    def test_with_example_data(self) -> None:
        """Test with the provided example data files."""
        data_dir = Path(__file__).parent.parent / "data"
        file1 = data_dir / "countries1.csv"
        file2 = data_dir / "countries2.csv"
        if not file1.exists() or not file2.exists():
            pytest.skip("Example data files not found")

        result = run_script(
            "--files", str(file1), str(file2), "--report", "average-gdp"
        )

        assert result.returncode == 0
        assert "United States" in result.stdout
        assert "China" in result.stdout
        assert "Japan" in result.stdout
