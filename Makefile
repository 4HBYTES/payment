SHELL:=/bin/bash
APP_DIR=./src/
all: install test

server:
	cd $(APP_DIR) && python manage.py runserver

install:
	virtualenv env
	source env/bin/activate
	pip install -r src/requirements.txt
	pip install -r src/requirements-extra.txt
	pip install -r src/tests/requirements.txt

test: lint test-unit

test-unit:
	nosetests --with-coverage --cover-package=src -w $(APP_DIR)

lint:
	python ./tools/pylint-recursive.py $(APP_DIR)
	flake8 $(APP_DIR)
