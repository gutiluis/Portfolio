

## Flask-SQLAlchemy
- __tablename__ is assumed with flasksqlalchemy extension within the model
- flask sqlalchemy manages a session per request. open, add, commit or rollback, and session closed()

## SQLAlchemy
- db_column_model
- imperative mapping and declarative mapping

## Flask:
- render_template
- url_for:
- send-subbmit the html form. not just leave it in the browser user-agent as a post request
- used to implement an internal flask route function
- redirect
- request context
- proxy
- access incoming request data after using url_for and GET and POST methods
- app context(). create_all()

## Jinja2 with Flask:
- for loops
- blocks
- the child file does not have body, or head html tags
- cannot define twice a block in the base
- only if the child has new code the layout should have a block
- use double quotes for html attributes
- order of attributes does not matter. however there is a convention
- Automatic autoescaping in jinja templates

## Bootstrap:
- css framework with optional javascript
- <link> tag inside the head for css
- <scrip></script> tag for javascript
- use bootstrap in head and body before closing the body
- bundle: modals, dropdowns, collapse, tooltips, popovers, carousel
- subresource integrity (SRI)
- bootstrap.css classes
- bootstap.js
- removed crossorigin and integrity hash

## CSS:
- At-rules
- keyframes
- mediaqueries

## HTML with Flask:
- the same name of the form attribute should be used with sqlalchemy when creating the model object instance
- within the form the required attribute does not affect the nullable=false within the sqlalchemy model

## HTTP with Flask:
- 302 found request post, 200, 304
- cache
- GET, POST
- URI

## use not null to force the column always have input

## aplying an href to an anchor changes the font. the goal is using an url_for flask route

## difference between string parse time and string parse format time
- model needs a datetime object. strptime

## get appearse in the browser. post doesnt

## using strftime within jinja template to display only year and month

## value does not work with jinja from the form in textarea tags
- In HTML, the initial content of a <textarea> is specified between its opening and closing tags, not as a value attribute.

## PSYCOPG:
### Psyscopg module is a postgresql db adapter for python
### several threads can share the same connection
### dialect provides asynchronous and synchronous implementations and notifications # psycopg3 module

### import dotenv to load_env() and connect the db the sqlclchemy postgresql supabase string

### check supabase db is made before running the flask server
### check if db exists
- npx supabase projects list # login to supabase cli
- npx supabase login
- npx supabase link
### supabase does not always expose raw db hosts via public dns # ping did not work for instance
### do not make the supabase db public use the pooler
- brew install libpq
- pip install python-dotenv sqlalchemy psycopg2

### The transaction mode connection string connects to your Postgres instance via a proxy which serves as a connection pooler. This is ideal for serverless or edge functions, which require many transient connections.

### can run raw sql from terminal cli or from supabase into the supabase db
### fix row level security in postgresql
### Supabase allows convenient and secure data access from the browser, as long as you enable RLS.
### Each policy is attached to a table, and the policy is executed every time a table is accessed.
### What auth.uid() is
### auth.uid() in RLS policies returns the UUID of the currently authenticated user.
### If no user is logged in (unauthenticated request), it returns NULL.
### `auth.uid()` Returns `null` When Unauthenticated
- USING (auth.uid() = user_id)
### When a request is made without an authenticated user (e.g., no access token is provided or the session has expired), auth.uid() returns null.
### explicitly checking for authentication
### authenticated and unauthenticated roles:
### anon: not logged in
### authenticated: logged in
### Any table that RLS will protect must have the user_id column filled with the actual owner’s UUID, or users won’t be able to access their data at all.
### if there are no more users there is no need for policies


# connection test with supabase
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- python3 test_supabase.py

### projects table is in the default public schema (normal) which can be accessed by anyone
### run in SQL to fix:
- ALTER TABLE projects ENABLE ROW LEVEL SECURITY;

## API keys:
### supabase BaaS
- publishable key # safe to expose
- secret keys # used in backend componends only. # row level security # never expose
- anon # jwt long lived
- service_role # jwt long lived # never expose

## both supabase and flask handle authentication
## flask needs authentication built by oneself. supabase does not authentication is built-in
## Flask has full control, custom logic

## flask error handling not for normal control flow
## not to replace validation
## not to hide bugs permanently
## error handling in flask is for exceptions

## request in flask
- class flask.Request(environ, populate_request=True, shallow=False)¶
- property form: ImmutableMultiDict[str, str]
- The form parameters. By default an ImmutableMultiDict is returned from this function. This can be changed by setting parameter_storage_class to a different type. This might be necessary if the order of the form data is important.

## get_or_404(ident(Any), description=None) with Flask
- Like get() but aborts with a 404 Not Found error instead of returning None.

## Building custom error pages in flask:
https://flask.palletsprojects.com/en/2.2.x/errorhandling/?highlight=error%20page#custom-error-pages



## supabase is not a framework is a backend-as-a-service(BaaS)
## in BaaS the backend services are built-in already
## authentication users, login, OAuth, JWT
## auto-generated REST and realtime APIs
## File storage
## Row Level Security
## Edge functions
### Every Supabase project includes a connection pooler
### every supabase project includes a connection string used in flask

### after connecting the models, tables and supabase you can either run sql commands from supabase gui, or supabase terminal, or psql terminal, or psycopg in python language
### tables need policies and Row level security

### can use supabase to host the webpage without running flask or cloudflare
### https://<project-ref>.supabase.co
### supabase url needs to specify the api endpoint
### supabase is automatically a REST endpoint (representational state transfer api):
### PostgreSQL as the backend – Supabase uses PostgreSQL to store your tables.
### PostgREST layer – Supabase runs a tool called PostgREST on top of your database. This exposes each table as a RESTful API.
### Automatic endpoints – For every table in your database, you get endpoints like:
### to view the tables from supabase it needs to fetch with javascript and tables need reading permission and RL enabled. suppabase has only tables no routes, no html, no css is a RESTful API
- check_if_reading_enabled_with_RLS.py



---

## cloudflare wrangler # deploy cloud workers should be first?
- npx wrangler --version
- npx wrangler dev # start local dev server # see .env
- npm create cloudflare@latest -- my-first-worker # create a new worker project with a cloudflare account and node.js
- npm run deploy # after myfisrtcloudflare app created # outside the worker env

## after running npm create cloudflare@latest -- my-first-worker. C3 will create a my-first-worker folder with a new package.json and wrangler.jsonc, a new .gitignore file too
## a workers project javascript makes it simpler than typescript. less code. easy debugging. less tooling
## js has request handling, edge runtime, kv/d1/r2, apis instead of ts toolchains
## the create-cloudflare worker template can be converted to ts later
## use ts for production not js
## use ts with supabase in production

## the worker has its own environment and local server with npx wrangler dev. cd my-mirst-worker && npx wrangler dev to run server

## each worker server instance is separate

## most developers prefer push code to github first and manual wrangler deploys cli than using cloudflare gitub deployment








---
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
