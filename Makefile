.PHONY: install test cov lint typecheck aaa check run clean

install: ## Install all dependencies
	uv sync

test: ## Run tests
	uv run pytest -v

cov: ## Run tests with coverage report
	uv run pytest --cov=csv_reports --cov-report=term-missing

lint: ## Run ruff linter
	uv run ruff check src/ tests/

typecheck: ## Run mypy type checker
	uv run mypy

aaa: ## Check AAA pattern in tests
	uv run flake8 --select=AAA tests/

check: lint typecheck aaa test ## Run all checks (lint + typecheck + AAA + tests)

run: ## Run with example data: make run FILES="data/countries1.csv data/countries2.csv" REPORT=average-gdp
	uv run python -m csv_reports --files $(FILES) --report $(REPORT)

clean: ## Remove build artifacts and caches
	rm -rf .mypy_cache .pytest_cache .ruff_cache .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
