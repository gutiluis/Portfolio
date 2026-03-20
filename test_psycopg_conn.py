#!/bin/env python3
'''
Script to test connection between the client and the postgresql db inside supabase with 
psycopg and python

'''
import psycopg
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment not in .env")

try:
    with psycopg.connect(DATABASE_URL) as conn:
        print("connection managed!")
        with conn.cursor() as cur: # declare a cursor that defines a result set
            cur.execute("SELECT version();")
            version = cur.fetchone()
            print("PostgreSQL version:", version)
# it is not mandatory to call the base class for the psycopg library
except psycopg.Error as error: # psycopg.Error is the baseclases for all errors
    print("Db conn err. The exception is Database error or OperationalError", error)