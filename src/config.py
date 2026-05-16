from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
RESULTS_DIR = DATA_DIR / "results"
FIGURES_DIR = PROJECT_ROOT / "figures"

AB_DATA_PATH = RAW_DIR / "ab_data.csv"
COUNTRY_DATA_PATH = RAW_DIR / "countries.csv"
CLEANED_DATA_PATH = PROCESSED_DIR / "dataset_cleaned.csv"