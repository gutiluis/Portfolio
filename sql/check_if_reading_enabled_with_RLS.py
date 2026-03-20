#!/bin/env python

'''
script to enforce read-only policy
enable RLS with python psycopg in existing table
removes any existing read policy (clean reset)
adds a select-only policy
using the database_url from .env
create a policy to allow public reading
'''

from dotenv import load_dotenv
import os
import psycopg

# or with pathlib and import a relative path or absolute path .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")  # make sure it's set

sql = """
ALTER TABLE projects ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Allow public read" ON projects;

CREATE POLICY "Allow public read"
ON projects
FOR SELECT
USING (true);
"""

try:
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
    print("RLS read-only policy enforces for the table")
except Exception as error:
    print("Error:", error)