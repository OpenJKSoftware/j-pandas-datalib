
lint:
	poetry run isort src
	poetry run pylint src
	poetry run black src
	poetry run flake8 src

test:
	poetry run pytest src/tests
