from pathlib import Path
from unittest.mock import patch

import pytest

from csv_reports.__main__ import main


def test_main_runs_successfully(
    sample_csv: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    argv = ["prog", "--files", str(sample_csv), "--report", "average-gdp"]
    with patch("sys.argv", argv):
        main()

    result = capsys.readouterr()

    assert "CountryA" in result.out
    assert "CountryB" in result.out
