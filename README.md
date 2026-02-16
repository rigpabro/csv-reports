# csv-reports

CLI-инструмент для формирования отчётов по макроэкономическим данным из CSV-файлов.

## Установка

Требуется Python 3.12+.

```bash
# С помощью uv (рекомендуется)
uv sync

# Или через pip
pip install -e .
```

## Использование

```bash
uv run csv-reports --files <file1.csv> [file2.csv ...] --report <название-отчёта>
```

### Доступные отчёты

- `average-gdp` — среднее ВВП по странам, сортировка по убыванию

### Пример запуска

```bash
uv run csv-reports --files data/countries1.csv data/countries2.csv --report average-gdp
```

Вывод:

```
+-----+----------------+---------------+
|   # | Country        |   Average GDP |
+=====+================+===============+
|   1 | United States  |      23923.7  |
+-----+----------------+---------------+
|   2 | China          |      17810.3  |
+-----+----------------+---------------+
|   3 | Japan          |       4497.67 |
+-----+----------------+---------------+
|   4 | Germany        |       4138.33 |
+-----+----------------+---------------+
|   5 | United Kingdom |       3100    |
+-----+----------------+---------------+
|   6 | France         |       2841    |
+-----+----------------+---------------+
```

## Добавление нового отчёта

1. Создать файл в `src/csv_reports/reports/`, например `population_by_continent.py`
2. Унаследоваться от `Report`, реализовать свойство `headers` и метод `generate`
3. Зарегистрировать через `@registry.register("название-отчёта")`
4. Импортировать модуль в `src/csv_reports/reports/__init__.py`

```python
from csv_reports.models import CountryRow
from csv_reports.reports import Report, registry


@registry.register("population-by-continent")
class PopulationByContinentReport(Report):
    @property
    def headers(self) -> list[str]:
        return ["Continent", "Total Population"]

    def generate(self, data: list[CountryRow]) -> list[list]:
        # логика отчёта
        return rows
```

## Тесты

```bash
make test        # запуск тестов
make cov         # тесты с отчётом о покрытии
```

## Проверки кода

```bash
make check       # ruff + mypy + flake8-aaa + pytest — всё разом
make lint        # только ruff
make typecheck   # только mypy
make aaa         # только flake8-aaa (AAA-паттерн в тестах)
```
