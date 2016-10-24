Master:

[![Master Build Status](https://travis-ci.com/icflix-hub/auth.svg?token=nv4RRLczqJcogRo4WLpU&branch=master)](https://travis-ci.com/icflix-hub/auth)
[![Master Coverage Status](https://coveralls.io/repos/github/icflix-hub/auth/badge.svg?branch=master&t=4rBKCh)](https://coveralls.io/github/icflix-hub/auth?branch=master)

Develop:

[![Develop Build Status](https://travis-ci.com/icflix-hub/ic-three.svg?token=nv4RRLczqJcogRo4WLpU&branch=develop)](https://travis-ci.com/icflix-hub/auth)
[![Develop Coverage Status](https://coveralls.io/repos/github/icflix-hub/auth/badge.svg?branch=develop&t=4rBKCh)](https://coveralls.io/github/icflix-hub/auth?branch=develop)


This is the auth application responsible for signin and signup.

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
 * `SECRET_KEY: String` Secret key of the application, make sure to change it every time you make a new project
 * `LOGENTRIES_TOKEN: String` Token for logentries service, can be left empty when developing locally
 * `OAUTH_API: String` Base URL for the oauth API
 * `OAUTH_APP_TOKEN: String` Application token to use 'old' services behind oauth
 * `OAUTH_API: String` Oauth API endpoint
 * `BILLING_API: String` Billing API endpoint
 * `USER_API: String` User API endpoint
 * `SMS_API: String` Sms Gateway API endpoint
 * `PRODUCTS_API: String` Products API endpoint
 * `APP_NAME: String` Application's name
 * `ENVIRONMENT: String` Application's environment (staging, production or testing)
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
curl http://localhost:5000/health/\?token\=053c4071-a683-4cbf-831d-394e6be95482
```

### License

ICFLIX 
