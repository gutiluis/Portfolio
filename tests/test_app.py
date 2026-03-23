#!/bin/env python3

"""
actual test
"""


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
