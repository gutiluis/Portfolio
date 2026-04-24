#!/bin/env python3

"""
Connection to Postgres db with supabase using a connection string,
type sqlalchemy,
source primary db,
method transaction pooler
"""

from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("SUPABASE_DB_USER")
PASSWORD = os.getenv("SUPABASE_DB_PASSWORD")
HOST = os.getenv("SUPABASE_DB_HOST")
PORT = os.getenv("SUPABASE_DB_PORT")
DBNAME = os.getenv("SUPABASE_DB_NAME")

# Construct the SQLAlchemy connection string
DATABASE_URL = (
    # ssl is a sqlalchemy connection argument named sslmode,
    # for controlling its behavior regarding secure (SSL) connections
    # secure socket layer
    # sslmode=require may be used to ensure that only secure
    # connections are established.
    f"postgresql+psycopg://{USER}:"
    f"{PASSWORD}@"
    f"{HOST}:"
    f"{PORT}/"
    f"{DBNAME}?sslmode=require"
)
# If using Transaction Pooler or Session Pooler,
# ensure disable SQLAlchemy client side pooling
engine = create_engine(DATABASE_URL, poolclass=NullPool)

try:
    with engine.connect() as conn:
        print("Connection successful!")
except Exception as error:
    print(f"Failed to connect: {error}")
