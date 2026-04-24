


# Architecture ### high level design, not libary usage
### Overview

This project is a web application for managing portfolio projects.
It follows a simple **client → API → database architecture** where the frontend interacts with backend endpoints that store and retrieve data from a database.

The architecture is designed to:

* Keep frontend and backend responsibilities separate
* Allow database access through secure API endpoints
* Enable future deployment to cloud infrastructure

Flask-Admin and REST endpoints
1. Model (Project)
2. Test model
3. Admin CRUD (Flask-Admin)
4. API endpoints
5. Test API

---

### System Architecture:

### Backend
- RESTful API Development: Designing the routes and endpoints that allow the frontend to communicate with the backend.

- Server-Side Rendering (SSR): Using Jinja2 to dynamically generate HTML, which is a key skill for SEO-friendly web applications.

- Authentication & Session Management: If your app has a login, you’ve mastered handling user states and secure cookies.

---

### Database Management:
- Object-Relational Mapping (ORM): The ability to interact with a database using Python objects rather than raw SQL.

- Database Migrations: Handling changes to your data structure over time (likely using tools like Flask-Migrate).

---

### Project Structure; TODO

```
```

### Key Directories; TODO

**app/**
Contains the main application logic including routes, models, and templates.

**tests/**
Unit and integration tests written with `pytest`.

**docs/**
Project documentation including architecture and testing documentation.

**.github/workflows/**
Continuous integration pipelines using GitHub Actions.

---

## Components

### Frontend

The frontend consists of:

* HTML templates
* CSS styling

---

## Backend (Flask)

The backend is responsible for:

* Routing HTTP requests
* Validating user input
* Handling API endpoints
* Communicating with the database

Example endpoints:

```
GET /projects
POST /projects
GET /projects/<id>
```

---

## Database (Supabase)

The database stores application data such as:

```
projects
├── id
├── title
├── description
├── created_at
```

Supabase provides:

* PostgreSQL database
* REST API access
* Row Level Security (RLS)

---

### Data Flow

Example workflow when a user creates a project:

1. User fills out a form in the frontend.
2. The frontend sends a `POST` request to the Flask API.
3. Flask validates the request.
4. Flask inserts the data into the Supabase PostgreSQL database.
5. A response is returned to the frontend.

---

### Deployment

Local development:

```
Developer Machine
│
├── Flask Development Server
└── Supabase Database
```

Production deployment may include:

```
Cloudflare
│
├── Static Frontend Hosting
└── API Backend
     │
     └── Supabase Database
```

---

### Design Decisions

### Flask for Backend

Flask was chosen because it is lightweight and allows full control over routing and API endpoints.

### Supabase for Database

Supabase provides a managed PostgreSQL database with built-in REST APIs and Row Level Security.

### Pytest for Testing

Pytest provides a simple framework for unit and integration testing of Flask endpoints.

---

### References:
[SQLAlchemy connection pooling docs](https://docs.sqlalchemy.org/en/20/core/pooling.html)
