import pandas as pd
import logging

from pathlib import Path

# ===== Logging Configuration =====
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

#===== File path =====
BASE_DIR = Path(__file__).resolve().parents[2]

RAW_FILE = BASE_DIR / "data" / "raw" / "Adidas_US_Sales.xlsx"

CLEANED_CSV = BASE_DIR / "data" / "cleaned" / "Adidas_US_Sales_Cleaned.csv"

CLEANED_XLSX = BASE_DIR / "data" / "cleaned" / "Adidas_US_Sales_Cleaned.xlsx"

#===== Load data =====
def load_data(file_path):

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
def clean_data(df):

    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
    )

    logging.info("Column Names Cleaned Successfully!")

    # Remove empty rows
    df = df.dropna(how="all")

    # Remove duplicates
    df = df.drop_duplicates()
    logging.info("Duplicates Removed Successfully!")

    # Checking missing values
    missing_values = df.isnull().sum()
    logging.info(f"Missing Values:\n{missing_values}")

    # Convert date features
    df["Invoice Date"] = pd.to_datetime(
        df["Invoice Date"],
        errors="coerce"
    )

    # Create date feature
    df["Year"] = df["Invoice Date"].dt.year
    df["Month"] = df["Invoice Date"].dt.month
    df["Day"] = df["Invoice Date"].dt.day

    logging.info("Dates standardized Successfully!")

    # Convert numeric columns
    numeric_cols = [
        "Price per Unit",
        "Units Sold",
        "Total Sales",
        "Operating Profit",
        "Operating Margin"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    logging.info("Numeric Columns Converted Successfully!")

    # Normalize categorical columns
    categorical_cols = [
        "Retailer",
        "Region",
        "City",
        "State"
    ]

    for col in categorical_cols:
        df[col] = (
            df[col]
            .astype(str)
            .str.lower()
            .str.strip()
        )

    logging.info("Categorical Columns Normalized Successfully!")

    return df

# ===== Save Data =====
def save_data(df):
    CLEANED_CSV.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(CLEANED_CSV, index=False)
    logging.info(f"\nCleaned Data Saved at {CLEANED_CSV}")

    CLEANED_XLSX.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_excel(CLEANED_XLSX, index=False)
    logging.info(f"\nCleaned Data Saved at {CLEANED_XLSX}!")
    
# ===== Main =====
def main():

    df = load_data(RAW_FILE)

    df = clean_data(df)

    save_data(df)

    logging.info("\nData Cleaning Process Completed Successfully!")

if __name__ == "__main__":
    main()