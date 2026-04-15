
This single script demonstrates:
REST endpoints (/users)
HTTP methods (GET, POST, PUT, PATCH, DELETE)
Query params (?name=luis)
Path params (/users/1)
RPC-style (/login)
Auth-protected (/protected)
File handling (/upload, /download)
Health check (/health)



api endpointS:
types of http methods in api endpoints:
GET, POST, PUT, PATCH, DELETE
GET /users
POST /users/1
DELETE /users/1
POST /createUser
POST /login
POST /sendEmail
# API endpoint in access level and permissions
- no auth needed
# JSON
/images/123.jpg

---

# `app` is the application is instance of the app# fix the only admin no users authentication. flask-login expects a user object
# db = SQLAlchemy(app)
# app is an object instance of the Flask class from the Flask library
# flask is the blueprint
# from flask import Flask
# app = Flask(__name__)
---

# Enable testing mode. Exceptions are propagated rather than handled by the the app’s error handlers. Extensions may also change their behavior to facilitate easier testing. You should enable this in your own tests.
# app.config["TESTING"] = True

---
1. Configure SQLAlchemy databases and models with app.config() to tell which db to use
2. Define models (tables) database schema
3. Run migrations / create tables
4. Write tests for th databases and models
5. Implement routes / API logic

---
### main entry points
- app/__init__.py application factory
- run.py development server
- tests/conftest.py test app


---
### application context vs request context vs context manager
- python with context managers
- flask application context current_app() proxy
db.sesion, db.engine, app.current_app(), g()
- flask request context

### use the context manager when the code runs outside flask's http requests. push it manually
see runtimeerror: working outside of application context
- __enter__()
- __exit__()

### use the application context manager to interact with the db and db.session
### application context
- know which flask extensions and helpers can know which flask application is currently active
- storing g object data
- prevent circular import issues using the current_app proxy
- access views
An active Flask application context is required to make queries and to access db.engine and db.session. This is because the session is scoped to the context so that it is cleaned up properly after every request or CLI command.
### flask sqlalchemy application context:
https://flask-sqlalchemy.readthedocs.io/en/stable/contexts/
### context manager reference with flasks:
https://flask.palletsprojects.com/en/stable/appcontext/
### with statement references:
https://peps.python.org/pep-0343/#use-cases

### examples of configurations and configuraton handling in flask:
settings you might want to change depending on the application environment like toggling the -debug mode, -setting the secret key, and other such environment-specific things.
### configuration values in handling configuration

---
## Linting

This project uses `pre-commit` hooks to enforce code style and quality locally.
When you commit, the hooks automatically run linters like Black and Flake8.

**Note:** GitHub Actions also runs the same linters in CI.
It is normal for linting to run again on GitHub even if it passed locally.
This ensures all code in the repo meets the required standards.

---

### PEP 8, 257, 405

### authentication and authorization
### authentication token should be in the http session so the server should be able to detect if the requester is admin or not
### session, flask-login, and abort in server to prevent user access

### UI restriction of api endpoints


### flask admin:
Flask-Admin automatically creates all the CRUD routes for Project inside the admin interface.
You don’t need @app.route("/projects/new") or similar for the admin interface.
It handles:
Listing entries (/admin/project/)
Creating entries (/admin/project/new/)
Editing entries (/admin/project/edit/<id>/)
Deleting entries (/admin/project/delete/<id>/)
All these routes are inside the /admin URL namespace by default.

Flask-Admin gives you a web interface for CRUD: create, read, update, delete rows in your tables.
or interact with the table directly with sql, supabase, postgresql

### initialize flask admin empty interface
### admin model views

### flask-basic auth
https://flask-basicauth.readthedocs.io/en/latest/

### flask-admin reference:
https://flask-admin.readthedocs.io/en/stable/introduction/
