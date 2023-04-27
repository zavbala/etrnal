format:
	isort --force-single-line-imports src tests
	black src tests
	isort src tests

dev:
	flask run --port=8000 --with-threads

deps:
	poetry export --without-hashes > requirements.txt

build:
	docker build -t etrnal-api .

docker:
	docker run -p 8000:8000 etrnal-api