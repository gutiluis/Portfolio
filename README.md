# Portfolio with SQLAlchemy, HTML, CSS, Cloudflare, Supabase, PostgreSQL



## How it works:
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- python3 app.py

---

## Tech Stack:

- Python
- Flask
- SQLAlchemy
- Jinja2
- HTML
- CSS
- Node.js
- PostgreSQL
- Cloudflare
- Supabase
- Psycopg

---

## Skills:
- Backend Architecture: Developed a modular server using Flask and Python, implementing Jinja2 for dynamic content rendering.

- Data Persistence: Architected a relational database schema using PostgreSQL and managed complex queries via SQLAlchemy ORM.

- Cloud Infrastructure: Optimized site delivery and security using Cloudflare for DNS management and SSL encryption.

### Backend
- RESTful API Development: Designing the routes and endpoints that allow the frontend to communicate with the backend.

- Server-Side Rendering (SSR): Using Jinja2 to dynamically generate HTML, which is a key skill for SEO-friendly web applications.

- Authentication & Session Management: If your app has a login, you’ve mastered handling user states and secure cookies.

### Database Management:
- Object-Relational Mapping (ORM): The ability to interact with a database using Python objects rather than raw SQL.

- Schema Design & Data Modeling: Defining relationships (One-to-Many, Many-to-Many) between tables.

- Database Migrations: Handling changes to your data structure over time (likely using tools like Flask-Migrate).

### Frontend & UI/UX:

- Responsive Web Design: Ensuring the app looks good on both mobile and desktop.

- Template Inheritence: Using Jinja2 to create reusable layouts (like a base.html), which demonstrates DRY (Don't Repeat Yourself) coding principles.

- Asset Optimization: Managing how CSS and scripts are loaded to keep the app fast.

### DevOps & Infrastructure
The inclusion of Cloudflare moves this from a "local script" to a "production-ready app."

- DNS & Domain Management: Configuring records to point your domain to your hosting provider.

- Web Security & Performance: Implementing SSL/TLS encryption, DDoS protection, and caching strategies.

- Deployment Pipelines: The knowledge required to take code from a local environment to a live URL.

---

## Features:
- RESTful backend built with Flask
- ORM database management using SQLAlchemy
- PostgreSQL database hosted on Supabase
- Dynamic HTML templates using Jinja2
- Responsive UI built with HTML and CSS
- CRUD operations for project management
- Secure environment configuration
- API integration

---

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

## clone:
```bash
git clone https://github.com/gutiluis/Portfolio.git
```