# A/B Testing Analysis for Checkout Page Design

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-150458.svg)
![SciPy](https://img.shields.io/badge/SciPy-Statistical_Testing-8CAAE6.svg)

## Project Overview

In e-commerce, the checkout page is a critical touchpoint in the user journey. Even minor design modifications can significantly impact whether users complete a purchase or abandon their carts. 

This repository contains an end-to-end A/B testing analysis designed to evaluate the performance of a newly redesigned checkout page against the existing one. The primary objective is to determine, with statistical significance, whether the new design drives a higher conversion rate.

### Hypothesis Testing
* **Null Hypothesis ($H_0$):** The new checkout page has the same or lower conversion rate compared to the old page.
* **Alternative Hypothesis ($H_1$):** The new checkout page has a higher conversion rate compared to the old page.

### Experimental Design
The project compares two variants:
| Group | Page Version | Description |
| :--- | :--- | :--- |
| **Control** | `old_page` | The existing checkout page design. |
| **Treatment**| `new_page` | The redesigned checkout page. |

**Primary Outcome Variable:**
* `converted = 1` → User converted (successfully completed the purchase).
* `converted = 0` → User did not convert (abandoned the process).

---

## Repository Structure

```text
A-B-Testing-Analysis-for-Checkout-Page-Design/
│
├── data/
│   ├── raw/                        # Original, immutable data files
│   │   ├── ab_test.csv
│   │   └── countries_ab.csv
│   │
│   ├── processed/                  # Cleaned datasets ready for analysis
│   │   └── dataset_cleaned.csv
│   │
│   └── results/                    # Exported metrics and statistical outputs
│       ├── conversion_summary.csv
│       ├── lift_summary.csv
│       └── ztest_results.csv
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb # Data cleaning and wrangling
│   └── 02_conversion_rate_ab_test.ipynb # EDA and Statistical Testing (Z-test)
│
├── src/                            # Source code for modularized functions
│   ├── __init__.py
│   └── config.py                   # Global configurations and file paths
│
├── figures/                        # Generated graphics and charts
│
├── reports/                        # Final analysis reports and presentations
│
├── README.md                       # Project documentation
├── requirements.txt                # Python dependencies
├── .gitignore                      # Ignored files for Git
└── main.py                         # Main execution script
