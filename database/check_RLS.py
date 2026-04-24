#!/bin/env python

"""
enable RLS with python psycopg
script usinng a venv to connect to the postgresql inside supabase
usind ethe database_url from .env
"""

from dotenv import load_dotenv
import os
import psycopg

# or with pathlib and import a relative path or absolute path .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")  # make sure it's set

with psycopg.connect(DATABASE_URL) as conn:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT relname AS table_name,
                   relrowsecurity AS rls_enabled
            FROM pg_class
            WHERE relname = 'projects';
        """)
        result = cur.fetchone()
        print(result)
