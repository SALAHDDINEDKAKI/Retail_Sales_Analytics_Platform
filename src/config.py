"""
Project configuration.

This module centralizes all commonly used file and folder paths.
Import these constants instead of recreating paths in every script.
"""

from pathlib import Path

# ===== Project Root =====
BASE_DIR = Path(__file__).resolve().parents[1]

# ===== Data Directories =====
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
CLEANED_DIR = DATA_DIR / "cleaned"

# ===== Data Files =====
RAW_FILE = RAW_DIR / "Adidas_US_Sales.xlsx"
CLEANED_CSV = CLEANED_DIR / "Adidas_US_Sales_Cleaned.csv"