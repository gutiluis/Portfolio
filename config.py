#!/bin/env python

"""
export environment variables for flask basic authentication keys

"""

import os

# import traceback


class Config:
    BASIC_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME")
    BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")
