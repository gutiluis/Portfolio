#!/bin/env python

"""
script for pytest
fixtures script for app factory
the script can do a setup, yield a value, do a teardown if configured
usually routes that use post method need a context manager for tests

fixture:
return value,
setup,
yield a value,
do teardown
see application factory..

# 3 main ways to test a flask route:
# automatically follow http redirects:
    # response = client.get("/", follow_redirect=True):
# submit real data requests
# test template_render


"""

from datetime import date
import pytest
import uuid

# add pytest to sys.path
# pytest only works if the directory
# that contains the app package is on sys.path
# tests need their own app instance
from app import create_app, db
import base64


# app routes need create_app()
# db.session interacts and need create_app()
@pytest.fixture
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",  # tests
            "BASIC_AUTH_USERNAME": "adminuser",
            "BASIC_AUTH_PASSWORD": "password",
        }
    )
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


# from docs
# client fixture used in api endpoints tests with pytest.
# what type of api endpoint is a test client flask?
@pytest.fixture
def client(app):  # test_app.py
    """client fixture used in public and admin api
    api endpoints tests with pytest"""
    return app.test_client()


@pytest.fixture
def auth_headers():  # test_app.py
    credentials = base64.b64encode(b"adminuser:password").decode("utf-8")
    return {"Authorization": f"Basic {credentials}"}


# fix name error create_dummy.. is not defined in test_...py file
# helper function too many repetition in pytest
# tests/conftest.py (add at the bottom)
@pytest.fixture
def create_dummy_project(app):
    """inmemory db for routes that need to post http"""

    def _create_dummy_project():  # underscore
        from app.models import Project
        from app import db

        with app.app_context():
            project = Project(
                title="title",
                #                created="date created",
                created=date(2024, 4, 1),
                description="description",
                skills="skills",
                github_repo="github repo",
            )
            db.session.add(project)
            db.session.commit()
            return project.id

    return _create_dummy_project


# route reads "date" from the form, converts it to a datetime.date,
# and passes it to the SQLAlchemy created column.
# That’s why in the test fixture you have to use "date", not "created" —


# the fixture is simulating the form submission,
# not the database column directly.
# use form names elements in .html
# make test data unique
@pytest.fixture
def form_post_project_request():
    """Returns a dictionary matching /admin/projects/new form fields."""
    unique = uuid.uuid4().hex[:6]  # '123456'

    return {
        "title": f"My New Project {unique}",
        "desc": "This is a test project",
        "skills": "Python, Flask",
        "github": f"https://github.com/test/{unique}",
        "date": "2024-04",  # must match your route's strptime("%Y-%m")
    }
