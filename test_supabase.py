#!/bin/env python3

'''
Connection to Postgres db with supabase using a connection string type sqlalchemy,
source primary db,
method transaction pooler
'''

from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("SUPABASE_DB_USER")
PASSWORD = os.getenv("SUPABASE_DB_PASSWORD")
HOST = os.getenv("SUPABASE_DB_HOST")
PORT = os.getenv("SUPABASE_DB_PORT")
DBNAME = os.getenv("SUPABASE_DB_NAME")

# Construct the SQLAlchemy connection string
DATABASE_URL = f"postgresql+psycopg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"
# If using Transaction Pooler or Session Pooler, we want to ensure we disable SQLAlchemy client side pooling -
# https://docs.sqlalchemy.org/en/20/core/pooling.html#switching-pool-implementations
# engine = create_engine(DATABASE_URL, poolclass=NullPool)
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        print("Connection successful!")
except Exception as error:
    print(f"Failed to connect: {error}")