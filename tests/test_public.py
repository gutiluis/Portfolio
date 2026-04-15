#!/bin/env python

"""
sending requests with the test client
test client makes requests to the application without running a live server

use client.post to manually push context like a real request,
instead of building an entire db. and simulate an http request
client.post automatically uses app.app_context() underneath

create WSGI environments or request objects from arbitrary data.

public views pytest file
conftest dummy for project_detail id

"""

from flask import template_rendered


# template_rendered is only for inspecting what the template receives.
# template_rendered does not to really send data and files through the route
# no need to hard code text from inside the requests in this case templates
# scalable render template not text from the template
def test_index(client):
    rendered_templates = []

    def record(sender, template, context, **extra):
        rendered_templates.append(template.name)

    # client argument has app fixture underneath
    template_rendered.connect(record, client.application)

    response = client.get("/")  # uses db.query.all()
    template_rendered.disconnect(record, client.application)
    assert response.status_code == 200
    assert "index.html" in rendered_templates


"""
# or test which template was rendered
def test_index(client):
    response = client.get("/")  # request the public root route
    assert response.status_code == 200
#    assert b"Hello" in response.data  # or text that appears in index.html
"""


# sending requests with the test client from flask docs
def test_about_me(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data  # match content of about_me.html


# real data is not being sent to the inmemory nor to the db
# In-memory database is only needed if your code touches the DB
# test queries a table before creation
def test_project_detail(client, create_dummy_project):
    # use the helper to create a dummy project
    project_id = create_dummy_project()
    rendered_templates = []

    def record(sender, template, context, **extra):
        rendered_templates.append(template.name)

    template_rendered.connect(record, client.application)

    with client.application.app_context():
        response = client.get(f"/projects/{project_id}")
    template_rendered.disconnect(record, client.application)

    assert response.status_code == 200
    # or assert and match template content in bytes
    assert "detail.html" in rendered_templates
