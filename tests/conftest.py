from pathlib import Path

import pytest

SAMPLE_CSV_CONTENT = """\
country,year,gdp,gdp_growth,inflation,unemployment,population,continent
CountryA,2023,1000,2.0,3.0,5.0,100,ContinentX
CountryA,2022,900,1.5,2.5,5.5,99,ContinentX
CountryB,2023,500,3.0,4.0,6.0,50,ContinentY
CountryB,2022,400,2.5,3.5,6.5,49,ContinentY
"""

SAMPLE_CSV_CONTENT_2 = """\
country,year,gdp,gdp_growth,inflation,unemployment,population,continent
CountryA,2021,800,1.0,2.0,6.0,98,ContinentX
CountryC,2023,2000,5.0,1.0,3.0,200,ContinentZ
"""


@pytest.fixture
def sample_csv(tmp_path: Path) -> Path:
    path = tmp_path / "data1.csv"
    path.write_text(SAMPLE_CSV_CONTENT)
    return path


@pytest.fixture
def sample_csv_2(tmp_path: Path) -> Path:
    path = tmp_path / "data2.csv"
    path.write_text(SAMPLE_CSV_CONTENT_2)
    return path
