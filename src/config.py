from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
RESULTS_DIR = DATA_DIR / "results"
FIGURES_DIR = BASE_DIR / "figures"

AB_TEST_PATH = RAW_DATA_DIR / "ab_test.csv"
COUNTRIES_PATH = RAW_DATA_DIR / "countries_ab.csv"
CLEANED_DATA_PATH = PROCESSED_DATA_DIR / "dataset_cleaned.csv"

CONVERSION_SUMMARY_PATH = RESULTS_DIR / "conversion_summary.csv"
LIFT_SUMMARY_PATH = RESULTS_DIR / "lift_summary.csv"
ZTEST_RESULTS_PATH = RESULTS_DIR / "ztest_results.csv"

BOOTSTRAP_RESULTS_PATH = RESULTS_DIR / "bootstrap_results.csv"
BOOTSTRAP_SUMMARY_PATH = RESULTS_DIR / "bootstrap_summary.csv"

COUNTRY_SUMMARY_PATH = RESULTS_DIR / "country_summary.csv"
COUNTRY_UPLIFT_PATH = RESULTS_DIR / "country_uplift.csv"
COUNTRY_ZTEST_PATH = RESULTS_DIR / "country_ztest_results.csv"
COUNTRY_BOOTSTRAP_PATH = RESULTS_DIR / "country_bootstrap_summary.csv"
COUNTRY_FINAL_PATH = RESULTS_DIR / "country_final_results.csv"
