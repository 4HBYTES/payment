This is boilerplate/skeleton code for a flask application meant for a RESTful API (with http and json)

## Current features:

 * Decent general structure
 * Postgres integration through SQL Alchemy
 * SQL migrations with flask-migrate
 * Prod/Dev configuration in the environment
 * Clevercloud structure, deployment ready
 * Form validation with wtforms
 * Endpoint documented with flask-swagger
 * Test environment : unittest, nose, coverage

## Some goals/wanted features:

 * JSON logging on the stdout (12 factors app)

## Environment variables

 * `DEBUG: boolean` True will enable debug mode
 * `SQLALCHEMY_DATABASE_URI: String` Database URI
 * `SECRET_KEY: String` Secret key
 * `LOGENTRIES_TOKEN: String` Token for logentries service

## Curl examples

 * curl http://localhost:5000/page/ --data '{"title":"a", "content":"content is a"}'
 * curl http://localhost:5000/page/
 * curl http://localhost:5000/page/a
 * curl http://localhost:5000/page/a --data '{"title":"a", "content":"content is still about a"}' -X PUT
 * curl http://localhost:5000/page/a -X DELETE

## Documentation

Endpoints are documented using flask-swagger, each individuals endpoint must have swagger doc in YML format. The final json document can be reached at: http://localhost:5000/spec

## Tests

 Nose documentation: http://nose.readthedocs.io/en/latest/plugins/cover.html

 * Simple unit tests run: `nosetests`
 * Need to display stdout (print/logging/...): `nosetests --nocapture`
 * Need a code coverage report: `nosetests --with-coverage --cover-package=app`
 * Need a code coverage HTML report: add the flag `--cover-html` to the command above, a directory `cover` will be created in the current directory with an index.html

## Code style

 * PEP-8 is followed and asserted using flake8 linter. There is a .flake8 file at the root of app, most IDEs/text editors can use it to determine the preferences.
 * Currently, the setting E501 for the max length of lines is disabled, it can be customized using: `max-line-length = 120` in the configuration file.
 * If you need to disable a specific setting on a specific line, you can add an inline comment like: `example = lambda: 'example'  # noqa: E731`
 * But it is also possible to run this tool in command line, just go inside app and type: `flake8`
