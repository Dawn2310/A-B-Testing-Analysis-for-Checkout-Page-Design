# A/B Testing Analysis for Checkout Page Design

This repository contains the analysis for A/B testing on the checkout page design.

## Project Structure

```text
ab-testing-checkout-analysis/
|-- data/
|   |-- raw/
|   |-- processed/
|   |-- results/
|-- notebooks/
|-- src/
|-- figures/
|-- reports/
|-- requirements.txt
|-- README.md
|-- main.py
```

# A/B Testing Analysis for Checkout Page Design

## Project Overview

This project analyzes an e-commerce A/B testing experiment to evaluate whether a redesigned checkout page affects user conversion rate compared with the existing page.

The main objective is to determine whether the new page should be rolled out based on conversion rate, uplift, statistical testing, and follow-up segmentation analysis.

---

## Week 1: Data Preparation & Quality Checks

### Objective

The objective of Week 1 is to prepare a clean dataset for A/B testing analysis.

This includes:

- Loading the raw A/B testing dataset
- Loading the country dataset
- Checking missing values
- Checking duplicate users
- Checking consistency between experiment group and landing page
- Removing inconsistent assignment-page records
- Merging country information
- Saving the cleaned dataset

---

## Dataset

This project uses two raw datasets.

### 1. `ab_test.csv`

This is the main A/B testing dataset.

| Column | Description |
|---|---|
| `user_id` | Unique user identifier |
| `timestamp` | Time-related field from the dataset |
| `group` | Experiment group: `control` or `treatment` |
| `landing_page` | Page shown to the user: `old_page` or `new_page` |
| `converted` | Binary conversion outcome: `1` = converted, `0` = not converted |

### 2. `countries_ab.csv`

This dataset contains country information for each user.

| Column | Description |
|---|---|
| `user_id` | Unique user identifier |
| `country` | User country |

---

## A/B Test Logic

In a valid A/B testing setup:

| Group | Expected Landing Page |
|---|---|
| `control` | `old_page` |
| `treatment` | `new_page` |

The control group represents the existing page, while the treatment group receives the new page.

During data quality checking, inconsistent records were identified where:

- `control` users saw `new_page`
- `treatment` users saw `old_page`

These inconsistent assignment-page records were removed before analysis.

---

## Week 1 Processing Steps

The preprocessing notebook is:

```text
notebooks/data_preprocessing.ipynb

**## Week 2: Conversion Rate, Uplift & Hypothesis Testing**

**### Objective**

The objective of Week 2 is to evaluate whether the new checkout page affects user conversion rate compared with the old page.

After completing data preprocessing in Week 1, the cleaned dataset is used to calculate conversion metrics and perform statistical testing.

**This week focuses on:**

- Calculating conversion rate for `old_page`
- Calculating conversion rate for `new_page`
- Estimating absolute lift
- Estimating relative uplift
- Running a two-proportion z-test
- Saving the main A/B testing results

---

**## Input Data**

The input file for Week 2 is:

```text
data/processed/dataset_cleaned.csv
