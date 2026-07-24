"""
Clean the Adidas US Sales dataset.

Steps:
- Load raw Excel data
- Standardize column names
- Remove duplicates and empty rows
- Convert dates and numeric columns
- Normalize categorical values
- Export cleaned CSV
"""

import pandas as pd
from pathlib import Path
from config import RAW_FILE, CLEANED_CSV
import logging


# ===== Logging =====
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

# Maps the original Kaggle column names to clean snake_case names
COLUMN_MAP = {
    "Retailer": "retailer",
    "Retailer ID": "retailer_id",
    "Invoice Date": "invoice_date",
    "Region": "region",
    "State": "state",
    "City": "city",
    "Product": "product",
    "Price per Unit": "price_per_unit",
    "Units Sold": "units_sold",
    "Total Sales": "total_sales",
    "Operating Profit": "operating_profit",
    "Operating Margin": "operating_margin",
    "Sales Method": "sales_method",
}

#===== Load data =====
def load_data(file_path: Path) -> pd.DataFrame:

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )
    
    df = pd.read_excel(
        file_path,
        skiprows=4
    )

    logging.info("Data Loaded Successfully!")

    return df

#===== Data Cleaning =====
def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    # Remove leading/trailing spaces first
    df.columns = df.columns.str.strip()

    # Columns existence check
    required_columns = COLUMN_MAP.keys()

    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    # Clean column names
    df.columns = (df.columns.str.strip())
    df = df.rename(columns=COLUMN_MAP)

    logging.info("Column Names Cleaned Successfully!")

    # Remove empty rows
    df = df.dropna(how="all")

    # Remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    removed = before - len(df)

    logging.info(f"Removed {removed} duplicate rows.")

    # Checking missing values
    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if missing.empty:
        logging.info("No missing values found.")
    else:
        logging.info(f"Missing values:\n{missing}")

    # Convert date features
    df["invoice_date"] = pd.to_datetime(
        df["invoice_date"],
        errors="coerce"
    )

    # Create date feature
    df["year"] = df["invoice_date"].dt.year
    df["month"] = df["invoice_date"].dt.month
    df["day"] = df["invoice_date"].dt.day

    logging.info("Dates standardized Successfully!")

    # Convert numeric columns
    numeric_cols = [
        "price_per_unit",
        "units_sold",
        "total_sales",
        "operating_profit",
        "operating_margin"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    logging.info("Numeric Columns Converted Successfully!")

    # Normalize categorical columns
    categorical_cols = [
        "retailer",
        "region",
        "city",
        "state"
    ]

    for col in categorical_cols:
        df[col] = (
            df[col]
            .astype("string")
            .str.lower()
            .str.strip()
        )

    logging.info("Categorical Columns Normalized Successfully!")

    return df

# ===== Save Data =====
def save_data(df: pd.DataFrame) -> None:
    CLEANED_CSV.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(CLEANED_CSV, index=False, encoding="utf-8")
    logging.info(f"\nCleaned Data Saved at {CLEANED_CSV}")
    
# ===== Main =====
def main() -> None:

    df = load_data(RAW_FILE)

    df = clean_data(df)

    save_data(df)

    logging.info("\nData Cleaning Process Completed Successfully!")

if __name__ == "__main__":
    main()