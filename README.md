# Portfolio

![Status](https://img.shields.io/badge/Status-Under%20Development-orange?style=flat-square)


🚧 ***Project under development*** 🚧

---

### Overview
A Flask-based backend service that allows users to create, manage, and display portfolio projects, with an admin dashboard for content control.

Designed with a modular architecture, RESTful APIs, and PostgreSQL for persistent storage.

---

### Table of Contents
* [Tech Stack](#tech-stack)
* [Features](#features)
* [Getting Started](#setup)
* [API Examples](#api)
* [Task List](#to-do-list)
* [Architecture](#arch)

---
<a name="tech-stack"></a>
### Tech Stack
- Backend: Python, Flask, SQLAlchemy
- Database: PostgreSQL, Supabase
- Frontend: Jinja2, HTML, CSS
- CDN: Cloudflare

---
<a name="features"></a>
### Features
- RESTful API with structured routing
- Database abstraction using SQLAlchemy ORM
- CRUD operations for project management
- Server-side rendering with Jinja2 templates
- Responsive UI using reusable layouts
- Environment-based configuration for security

---
<a name="setup"></a>
### Getting Started
```bash
git clone https://github.com/gutiluis/Portfolio.git
cd Portfolio
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python3 run.py
```

---
<a name="api"></a>
### Example API Endpoints
#### Retrieve Project by ID
**GET** `/api/projects/<id>`

**Description:** Fetch a specific project.

#### Create Project
**POST** `/api/projects`

**Description:** Create a new project.

#### Delete Project by ID
**DELETE** `/api/projects/<id>`

**Description:** Remove a project by its ID.

---
<a name="to-do-list"></a>
### Task List
- [x] Flask local deployment
- [ ] Transition from werkzeug to Gunicorn/Nginx
- [ ] Oracle VM instance deployment
- [ ] Write docs
- [ ] Acquire domain
- [ ] Pentesting

---
<a name="arch"></a>
### Architecture
- The project follows a modular design pattern to ensure scalability and maintainability.

- Infrastructure: Hosted on an Oracle Cloud VM using a production-ready WSGI server.

- System Design: For a deep dive into the service layers, data flow, and component interaction, see the [Architecture Overview](/docs/ARCHITECTURE.md).

- Database: PostgreSQL/Supabase for persistent storage.

---

> [!IMPORTANT]
> Incomplete features behaviour might change[^1].

---

![License](https://img.shields.io/github/license/gutiluis/Portfolio?style=flat-square&color=blue)
### License
This project is licensed under the **MIT License**[^2].

---

[^1]: Currently building.
[^2]: See the [LICENSE](/gutiluis/Portfolio/blob/main/LICENSE) file for details.
