SHELL:=/bin/bash
APP_DIR=./app/
all: install test

server:
	cd $(APP_DIR) && python manage.py runserver

install:
	virtualenv env
	source env/bin/activate
	pip install -r app/requirements.txt
	pip install -r app/tests/requirements.txt

test: lint test-unit

test-unit:
	nosetests --with-coverage --cover-package=app -w $(APP_DIR)

lint:
	python ./tools/pylint-recursive.py $(APP_DIR)
	flake8 $(APP_DIR)
