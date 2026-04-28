# Portfolio

![Status](https://img.shields.io/badge/Status-Under%20Development-orange?style=flat-square)

🚧 ***Project under development*** 🚧

---

### Overview
A Flask-based backend service that allows users to create, manage, and display portfolio projects, with an admin dashboard for content control.

Designed with a modular architecture, RESTful APIs, and PostgreSQL for persistent storage.

---

### Tech Stack:
- Backend: Python, Flask, SQLAlchemy
- Database: PostgreSQL, Supabase
- Frontend: Jinja2, HTML, CSS
- CDN: Cloudflare

---

### Features:
- RESTful API with structured routing
- Database abstraction using SQLAlchemy ORM
- CRUD operations for project management
- Server-side rendering with Jinja2 templates
- Responsive UI using reusable layouts
- Environment-based configuration for security

---

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

### Architecture
- Modular separation of routes, models, and services
- ORM layer abstracts raw SQL queries
- Template inheritance using Jinja2 (DRY)

---

### Notes
Project features incomplete or may change[^1].

---

![License](https://img.shields.io/github/license/gutiluis/Scripts?style=flat-square&color=blue)
### License
This project is licensed under the **MIT License**[^2].

---

[^1]: Development phase under revision.
[^2]: See the [LICENSE](LICENSE) file for details.
