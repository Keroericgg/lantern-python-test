install:
	poetry install --no-root

dev:
	poetry run fastapi dev src/main.py

unit-test:
	poetry run python -m unittest discover -s tests/unit_tests

integration-test:
	poetry run pytest tests/integration_tests



.PHONY: install dev
