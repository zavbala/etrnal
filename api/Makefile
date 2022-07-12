format:
	isort --force-single-line-imports src tests
	black src tests
	isort src tests

dev:
	flask run --with-threads

build:
	poetry export --without-hashes > requirements.txt