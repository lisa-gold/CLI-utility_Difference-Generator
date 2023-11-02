build:
	poetry  build

publish: # публикация пакета без добавления его в  каталог PyPI
	poetry publish --dry-run

reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

gendiff: # run gendiff
	poetry run gendiff

lint: # run linter flake8
	poetry run flake8 gendiff

test: # run tests
	poetry run pytest

test-coverage: # form test-coverage report
	poetry run pytest --cov=gendiff --cov-report xml