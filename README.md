This is boilerplate/skeleton code for a flask application meant for a RESTful API (with http and json)

## Current features:

 * Decent general structure
 * Basic authentication module, with permissions and token auth
 * SQL migrations with flask-migrate

## Some goals/wanted features:

 * Prod/Dev configuration
 * Clevercloud structure
 * Use wtforms or other validation lib
 * Create services and implement DI
 * Setup test environment (unittest+nose+coverage)
 * Use swagger

## Environment variables

 * `DEBUG: boolean` True will enable debug mode
 * `SQLALCHEMY_DATABASE_URI: String` Database URI
 * `SECRET_KEY: String` Secret key

## Curl examples

 * curl http://localhost:5000/page/ --data '{"title":"a", "content":"content is a"}'
 * curl http://localhost:5000/page/
 * curl http://localhost:5000/page/a
 * curl http://localhost:5000/page/a --data '{"title":"a", "content":"content is still about a"}' -X PUT
 * curl http://localhost:5000/page/a -X DELETE

## Tests

 Nose documentation: http://nose.readthedocs.io/en/latest/plugins/cover.html

 * Simple unit tests run: `nosetests`
 * Need to display stdout (print/logging/...): `nosetests --nocapture`
 * Need a code coverage report: `nosetests --with-coverage --cover-package=app`
 * Need a code coverage HTML report: add the flag `--cover-html` to the command above, a directory `cover` will be created in the current directory with an index.html
