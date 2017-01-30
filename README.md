# Billing/payment API

Notes for archlinux users, as it requires python 2:

 * sudo pacman -S python2
 * sudo pacman -S python2-pip
 * sudo pip2.7 install virtualenv
 * virtualenv -p /usr/bin/python2 env
 * source env/bin/activate


Curl example:

curl http://127.0.0.1:5000/payment/paypal/init --data '{"product": "my-uuid-v4-xxx", "quantity": 2}' -v


Current problem:

The 302 redirect does not work, its returning a 200, don't know why


Next:

Create the endpoint to execute the payment (PAYPAL_RETURN_URL)

## Current features:

 * Decent general structure
 * Prod/Dev configuration in the environment
 * Clevercloud structure, deployment ready
 * Rollbar integration
 * Endpoint documented with flask-restplus
 * Test environment : unittest, nose, coverage
 * Travis integration for unit tests and coverage
 * CORS ready
 * JSON logging on the stdout and logentries

## Some goals/wanted features:

 * Create functionnal tests and run them separately from the unit tests

## Installation

This project requires pip and virtualenv.
```bash
make install
```

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
 * `ROLLBAR_ACCESS_TOKEN: String` Rollbar's app access token

## Documentation

Endpoints are documented using flask-restplus.
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
