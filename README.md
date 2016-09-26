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
