Master:

[![Master Build Status](https://travis-ci.com/icflix-hub/flask-boilerplate.svg?token=nv4RRLczqJcogRo4WLpU&branch=master)](https://travis-ci.com/icflix-hub/flask-boilerplate)
[![Master Coverage Status](https://coveralls.io/repos/github/icflix-hub/flask-boilerplate/badge.svg?branch=master&t=4rBKCh)](https://coveralls.io/github/icflix-hub/flask-boilerplate?branch=master)

Develop:

[![Develop Build Status](https://travis-ci.com/icflix-hub/ic-three.svg?token=nv4RRLczqJcogRo4WLpU&branch=develop)](https://travis-ci.com/icflix-hub/flask-boilerplate)
[![Develop Coverage Status](https://coveralls.io/repos/github/icflix-hub/flask-boilerplate/badge.svg?branch=develop&t=4rBKCh)](https://coveralls.io/github/icflix-hub/flask-boilerplate?branch=develop)


This is boilerplate/skeleton code for a flask application meant for a RESTful API (with http and json)

## Current features:

 * Decent general structure
 * Postgres integration through SQL Alchemy
 * SQL migrations with flask-migrate
 * Prod/Dev configuration in the environment
 * Clevercloud structure, deployment ready
 * Newrelic integration
 * Form validation with wtforms
 * Endpoint documented with flask-swagger
 * Test environment : unittest, nose, coverage
 * Travis integration for unit tests and coverage
 * CORS ready
 * JSON logging on the stdout and logentries

## Some goals/wanted features:

 * Create functionnal tests and run them separately from the unit tests (local postgres instance)

## Installation

This project requires pip and virtualenv.
```bash
make install
```

### Prepare a local database

Flask-Migrate documentation: https://flask-migrate.readthedocs.io/en/latest/

Install Postgres, create a database and a user, assign the permissions to it, then:

 * `python manage.py db upgrade`
 * `python manage.py db current` Optional, will simply display the current migration

If you modify your SQLAlchemy models, you can create a new migration by running:

 * `python manage.py db migrate`

You can then repeat the steps above to apply the migration and check the status. Make sure to always commit new migration files.

## Run
```bash
make server
```

## Environment variables

 * `DEBUG: boolean` True will enable debug mode, and display full stack trace and an interactive shell in the browser
 * `SQLALCHEMY_DATABASE_URI: String` Database URI, format -> rdbms://user:password@host:port/database
 * `SECRET_KEY: String` Secret key of the application, make sure to change it every time you make a new project
 * `LOGENTRIES_TOKEN: String` Token for logentries service, can be left empty when developing locally
 * `APP_NAME: String` Application's name
 * `ENVIRONMENT: String` Application's environment (staging or production)
 * `APP_TOKEN: String` Application's token


## Documentation

Endpoints are documented using flask-swagger, each individuals endpoint must have swagger doc in YML format.
The final json document can be reached at: http://localhost:5000/spec

## Tests

 Nose documentation: http://nose.readthedocs.io/en/latest/plugins/cover.html

 Simple unit tests run
```bash
make test-unit
```

## Code style and Linting 

 * Linting is using pylint and flake8.
 * PEP-8 is followed and asserted using flake8 linter. There is a .flake8 file at the root of app, most IDEs/text editors can use it to determine the preferences.
 
 To lint type 
```bash
make lint
```

## Curl examples
```bash
curl http://localhost:5000/page/ --data '{"title":"a", "content":"content is a"}'
curl http://localhost:5000/page/
curl http://localhost:5000/page/a
curl http://localhost:5000/page/a --data '{"title":"a", "content":"content is still about a"}' -X PUT
curl http://localhost:5000/page/a -X DELETE

```

### License

ICFLIX 
