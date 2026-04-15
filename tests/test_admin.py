#!/bin/env python3

"""

route/view public tets inside __init__.py and
private tests in blueprint with http authentication
Flask does not accept <int:project_id> in the URL when making a request.
<int:project_id> is a route parameter placeholder, not a literal string.
You need to replace it with a real integer ID when calling client.get().

assertions bytes/strings must be from the html renders

"""

from datetime import datetime

# from app.models import Project
# pytest automatically does the import of the fixture as a parameter
# from tests.conftest import form_post_project_request


# from flask docs
def test_admin_new_project_with_auth(
    client,
    auth_headers,
    form_post_project_request,  # add a comma
):
    """get"""
    response = client.get(
        # auth_headers must be passed as http headers not keyword args
        "/admin/projects/new",
        headers=auth_headers,
    )
    # response.data can be anything from the same html template with jinja
    assert response.status_code == 200

    """post"""
    response = client.post(
        "/admin/projects/new",
        headers=auth_headers,
        data=form_post_project_request,
        follow_redirects=True,
    )
    assert response.status_code == 200


def test_admin_new_project_without_auth(client):
    response = client.get("/admin/projects/new")
    assert response.status_code == 401  # unauthorized 401cd


# client fixture already uses app
# use client when sending requets ex: response = client.get("/")
def test_admin_edit_project_with_auth(
    client, auth_headers, create_dummy_project, form_post_project_request
):
    project_id = create_dummy_project()

    response = client.get(f"/admin/projects/{project_id}/edit", headers=auth_headers)
    assert response.status_code == 200
    assert b"<form action" in response.data
    # type of test and request
    response = client.post(
        f"/admin/projects/{project_id}/edit",
        headers=auth_headers,
        # form_post_project_request is a dictionary returned by the
        # form_post_project_request is a fixture when passed as an argument
        data=form_post_project_request,
        follow_redirects=True,
    )

    assert response.status_code == 200
    # return something from the html template
    assert b"Project Title" in response.data
    # assert b'<form action' in response.data
    # assert b'name="skills"' in response.data


def test_admin_edit_project_without_auth(client, create_dummy_project):
    project_id = create_dummy_project()
    response = client.get(f"/admin/projects/{project_id}/edit")
    assert response.status_code == 401


def test_admin_delete_project_with_auth(client, create_dummy_project):
    project_id = create_dummy_project()
    response = client.get(f"/admin/projects/{project_id}/delete")
    assert response.status_code == 401
    # assert b"Delete with authentication" in response.data


def test_admin_delete_project_without_auth(client, create_dummy_project):
    project_id = create_dummy_project()
    response = client.get(f"/admin/projects/{project_id}/delete")
    assert response.status_code == 401


print(datetime.time())
