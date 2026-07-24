"""
Load the cleaned Adidas Sales dataset into a PostgreSQL staging table.

Run this AFTER:
1. data_cleaning.py
2. Creating the database schema

The cleaned CSV is first loaded into a staging table.
SQL scripts can then populate the dimension and fact tables from
the staging table.
"""

import logging

import pandas as pd

from config import CLEANED_CSV
from db_connection import get_engine

# ===== Logging =====
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def load_to_postgres() -> None:
    """
    Load the cleaned CSV into the PostgreSQL staging table.
    """

    if not CLEANED_CSV.exists():
        raise FileNotFoundError(
            f"Cleaned dataset not found:\n{CLEANED_CSV}\n"
            "Run data_cleaning.py first."
        )

    logging.info("Reading cleaned CSV...")

    df = pd.read_csv(
        CLEANED_CSV,
        parse_dates=["invoice_date"]
    )

    logging.info(f"Loaded {len(df):,} records from CSV.")

    engine = get_engine()

    logging.info("Connecting to PostgreSQL...")

    df.to_sql(
        name="stg_retail_sales",
        con=engine,
        if_exists="replace",
        index=False
    )

    logging.info(
        f"Successfully loaded {len(df):,} rows into 'stg_retail_sales'."
    )


def main() -> None:
    load_to_postgres()


if __name__ == "__main__":
    main()