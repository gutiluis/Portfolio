# Architecture

## Overview

This project is a web application for managing portfolio projects.
It follows a simple **client → API → database architecture** where the frontend interacts with backend endpoints that store and retrieve data from a database.

The architecture is designed to:

* Keep frontend and backend responsibilities separate
* Allow database access through secure API endpoints
* Enable future deployment to cloud infrastructure

---

# System Architecture

```
User Browser
     │
     │ HTTP Requests
     ▼
Frontend (HTML / CSS / JavaScript)
     │
     │ API Calls (fetch / axios)
     ▼
Backend (Flask Application)
     │
     │ SQLAlchemy ORM
     ▼
Supabase Transaction Pooler (Supavisor / PgBouncer)
     │
     │ PostgreSQL protocol
     ▼
Database (Supabase PostgreSQL)


```

Optional production deployment:

```
User
 │
 ▼
Cloudflare (DNS / CDN)
 │
 ▼
Frontend Hosting
 │
 ▼
API Server (Flask)
 │
 ▼
Supabase PostgreSQL Database
```

---

# Project Structure

```
Portfolio/
│
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── routes.py
│   ├── models.py
│   └── templates/
│
├── tests/
│   ├── conftest.py
│   └── test_routes.py
│
├── docs/
│   ├── architecture.md
│   └── testing.md
│
├── .github/
│   └── workflows/
│
├── requirements.txt
├── README.md
└── setup.sh
```

### Key Directories

**app/**
Contains the main application logic including routes, models, and templates.

**tests/**
Unit and integration tests written with `pytest`.

**docs/**
Project documentation including architecture and testing documentation.

**.github/workflows/**
Continuous integration pipelines using GitHub Actions.

---

# Components

## Frontend

The frontend consists of:

* HTML templates
* CSS styling
* JavaScript for API calls

Responsibilities:

* Display portfolio projects
* Submit forms
* Fetch data from API endpoints

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

# Data Flow

Example workflow when a user creates a project:

1. User fills out a form in the frontend.
2. The frontend sends a `POST` request to the Flask API.
3. Flask validates the request.
4. Flask inserts the data into the Supabase PostgreSQL database.
5. A response is returned to the frontend.

---

# Technology Stack

Backend

* Python
* Flask
* psycopg / PostgreSQL driver

Database

* Supabase (PostgreSQL)

Frontend

* HTML
* CSS
* JavaScript

Testing

* pytest

Infrastructure

* Cloudflare (DNS / CDN)
* GitHub (version control)

---

# Deployment

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

# Design Decisions

### Flask for Backend

Flask was chosen because it is lightweight and allows full control over routing and API endpoints.

### Supabase for Database

Supabase provides a managed PostgreSQL database with built-in REST APIs and Row Level Security.

### Pytest for Testing

Pytest provides a simple framework for unit and integration testing of Flask endpoints.

---

# Future Improvements

* Replace Flask server with serverless functions
* Deploy frontend using Cloudflare Pages
* Add authentication with Supabase Auth
* Expand automated test coverage

### References:
[SQLAlchemy connection pooling docs](https://docs.sqlalchemy.org/en/20/core/pooling.html)
