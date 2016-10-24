SHELL:=/bin/bash

all: install test

server:
	cd app && python manage.py runserver

install:
	virtualenv env
	source env/bin/activate
	pip install -r app/requirements.txt
	pip install -r app/tests/requirements.txt

test: lint test-unit

test-unit:
	cd app && nosetests

lint:
	python ./tools/pylint-recursive.py app
	flake8 app
