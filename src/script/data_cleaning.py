import pandas as pd
from pathlib import Path

#===== File path =====
BASE_DIR = Path(__file__).resolve().parents[2]

RAW_FILE = BASE_DIR / "data" / "raw" / "Adidas_US_Sales.xlsx"

CLEANED_CSV = BASE_DIR / "data" / "cleaned" / "Adidas_US_Sales_Cleaned.csv"

CLEANED_XLSX = BASE_DIR / "data" / "cleaned" / "Adidas_US_Sales_Cleaned.xlsx"

#===== Load data =====
def load_data(file_path):
    df = pd.read_excel(file_path, skiprows=4)
    print("Data Loaded Successfully!")
    return df

#===== Data Cleaning =====
def clean_data(df):
    # Remove empty rows
    df = df.dropna(how="all")

    # Remove duplicates
    df = df.drop_duplicates()
    print("Duplicates Removed Successfully!")

    # Checking missing values
    missing_values = df.isnull().sum()
    print(f"Missing Values:\n{missing_values}")

    # Convert date features
    df["Invoice Date"] = pd.to_datetime(
        df["Invoice Date"],
        errors="coerce"
    )

    # Create date feature
    df["Year"] = df["Invoice Date"].dt.year
    df["Month"] = df["Invoice Date"].dt.month
    df["Day"] = df["Invoice Date"].dt.day

    print("Dates standardized Successfully!")

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

    print("Categorical Columns Normalized Successfully!")

    return df

# ===== Save Data =====
def save_data(df):
    CLEANED_CSV.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(CLEANED_CSV, index=False)
    print("\nCleaned Data Saved as CSV!")

    CLEANED_XLSX.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_excel(CLEANED_XLSX, index=False)
    print("\nCleaned Data Saved as XLSX!")
    
# ===== Main =====
def main():

    df = load_data(RAW_FILE)

    df = clean_data(df)

    save_data(df)

    print("\nData Cleaning Process Completed Successfully!")

if __name__ == "__main__":
    main()