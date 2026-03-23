#!/bin/env python

"""
script to enforce read-only policy
enable RLS with python psycopg in existing table
removes any existing read policy (clean reset)
adds a select-only policy
using the database_url from .env
create a policy to allow public reading

and check if reading is enabled
"""

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
    print("RLS read-only policy enforced for the table")
except Exception as error:
    print("Error:", error)

try:
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:

            # TEST READ (should work)
            cur.execute("SELECT * FROM projects;")
            print("READ OK:", cur.fetchall())

            # TEST WRITE (should fail)
            cur.execute("INSERT INTO projects (title) VALUES ('test');")

except Exception as error:
    print("Expected error on write:", error)
