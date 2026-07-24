"""
Reusable PostgreSQL connection helper.

Reads database credentials from the project's .env file and returns
a reusable SQLAlchemy engine.

Example:
    from db_connection import get_engine

    engine = get_engine()
"""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from config import BASE_DIR

# ===== Load environment variables =====
load_dotenv(BASE_DIR / ".env", encoding="utf-8-sig")


def get_engine() -> Engine:
    """
    Create and return a SQLAlchemy engine connected to PostgreSQL.
    """

    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    if not all([database, user, password]):
        raise ValueError(
            "Missing database credentials.\n"
            "Create a '.env' file from '.env.example' and "
            "fill in all required values."
        )

    connection_url = (
        f"postgresql://{user}:{password}"
        f"@{host}:{port}/{database}"
    )

    return create_engine(
        connection_url,
        pool_pre_ping=True
    )