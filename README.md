# A/B Testing Analysis for Checkout Page Design

This repository contains an A/B testing analysis for an e-commerce checkout page design.  
The goal is to evaluate whether a redesigned checkout page affects user conversion rate compared with the existing checkout page.

## Repository Structure

```text
A-B-Testing-Analysis-for-Checkout-Page-Design/
│
├── data/
│   ├── raw/
│   │   ├── ab_test.csv
│   │   └── countries_ab.csv
│   │
│   ├── processed/
│   │   └── dataset_cleaned.csv
│   │
│   └── results/
│       ├── conversion_summary.csv
│       ├── lift_summary.csv
│       └── ztest_results.csv
│
├── notebooks/
│   ├── data_preprocessing.ipynb
│   └── 02_conversion_rate_ab_test.ipynb
│
├── src/
│   ├── __init__.py
│   └── config.py
│
├── figures/
│
├── reports/
│
├── README.md
├── requirements.txt
├── .gitignore
└── main.py
---

## Project Overview

In e-commerce, the checkout page is one of the most important stages in the user journey. A small design change may affect whether users complete a purchase or leave without converting.

This project compares two page versions:

| Page | Description |
|---|---|
| `old_page` | Existing checkout page |
| `new_page` | Redesigned checkout page |

The main outcome variable is:

```text
converted = 1  → user converted / purchased / completed the target action
converted = 0  → user did not convert
