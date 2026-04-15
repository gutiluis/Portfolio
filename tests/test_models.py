#!/bin/env python3
# test model behavior

"""
deterministic tests same data
assertions predictable
helps catch regression

when to test ORM models:
flask testing docs
sqlalchemy testing examples
pytest plugins for db

other pytest plugins:
engine, connection, dbsession

# context manager per request. endpoints have it automatically
see runtimeerror working outside of application context

https://flask-sqlalchemy.readthedocs.io/en/stable/contexts/

"""

from app.models import Project
from app import db
from datetime import date


# does not need a database and
# test your app using the Flask test client to make requests to the endpoints
# the context will be available as part of the request.
def test_project_model(app):
    """application context test with manual context"""
    with app.app_context():
        project = Project(
            title="Test Project",
            # deterministic test
            created=date(2024, 2, 1),  # real model has year and month
            description="test desc",
            skills="python",
            github_repo="https://github.com/test/rep",
        )
        db.session.add(project)
        db.session.commit()

        assert Project.query.count() == 1
        assert Project.query.first().title == "Test Project"
