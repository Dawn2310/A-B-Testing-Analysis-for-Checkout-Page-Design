# A/B Testing Analysis for Checkout Page Design

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-150458.svg)
![Statsmodels](https://img.shields.io/badge/Statsmodels-Statistical_Modeling-green.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange.svg)

## Project Overview

In e-commerce, the checkout page is a critical touchpoint. Even minor design modifications can affect whether users complete a purchase or abandon the checkout process.

This repository contains an end-to-end A/B testing analysis to evaluate whether a redesigned checkout page (`new_page`) improves conversion rate compared with the existing checkout design (`old_page`).

The analysis combines:

- Data preprocessing and quality checks
- Conversion rate analysis
- Lift and uplift estimation
- Two-proportion z-test
- Bootstrap confidence intervals
- Country-level segmentation
- Country-level hypothesis testing
- Country-level bootstrap risk analysis
- Visualization
- Logistic regression modeling and diagnostics

**Final Business Recommendation:** Do not roll out the new page at this stage. The new design does not show statistically significant improvement in conversion rate, and the observed uplift is slightly negative. Further design iteration and additional testing are recommended before any full rollout decision.

---

## Research Problem

The core objective is to determine whether the difference in conversion rates between the old and new pages is statistically significant, or merely due to random variation.

The main hypothesis test is two-tailed:

- **Null Hypothesis (H₀):** The new checkout page has the same conversion rate as the old page.  
  `CR_new = CR_old`

- **Alternative Hypothesis (H₁):** The new checkout page has a different conversion rate compared with the old page.  
  `CR_new ≠ CR_old`

---

## Dataset

The analysis is based on two raw datasets.

### 1. `ab_data.csv`

This is the main A/B testing dataset.

| Column | Description |
|---|---|
| `user_id` | Unique identifier for each user |
| `timestamp` | Time-related field from the dataset |
| `group` | A/B test assignment: `control` or `treatment` |
| `landing_page` | Page actually seen by the user: `old_page` or `new_page` |
| `converted` | Binary outcome: `1` = purchased, `0` = did not purchase |

### 2. `countries.csv`

This dataset maps each `user_id` to a country.

| Column | Description |
|---|---|
| `user_id` | Unique identifier for each user |
| `country` | User country: US, UK, or CA |

---

## Repository Structure

```text
A-B-Testing-Analysis-for-Checkout-Page-Design/
│
├── index.html                              # Interactive HTML report (DAP391m)
│
├── data/
│   ├── raw/
│   │   ├── ab_data.csv                     # Raw A/B test data
│   │   └── countries.csv                   # Country mapping data
│   │
│   ├── processed/
│   │   └── dataset_cleaned.csv             # Cleaned and merged dataset
│   │
│   └── results/
│       ├── conversion_summary.csv
│       ├── lift_summary.csv
│       ├── ztest_results.csv
│       ├── bootstrap_results.csv
│       ├── bootstrap_summary.csv
│       ├── country_summary.csv
│       ├── country_uplift.csv
│       ├── country_ztest_results.csv
│       ├── country_bootstrap_summary.csv
│       ├── country_final_results.csv
│       ├── logistic_model_basic.csv
│       ├── logistic_model_country.csv
│       ├── logistic_model_time_adjusted.csv
│       ├── logistic_model_interaction.csv
│       ├── logistic_odds_ratios.csv
│       ├── logistic_model_comparison.csv
│       ├── logistic_vif_results.csv
│       └── logistic_vif_interaction_results.csv
│
├── results/                                # Duplicate results for quick access
│   ├── conversion_summary.csv
│   ├── lift_summary.csv
│   ├── ztest_results.csv
│   ├── bootstrap_results.csv
│   ├── bootstrap_summary.csv
│   ├── country_summary.csv
│   ├── country_uplift.csv
│   ├── country_ztest_results.csv
│   ├── country_bootstrap_summary.csv
│   └── country_final_results.csv
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_conversion_rate_ab_test.ipynb
│   ├── 03_bootstrap_confidence_interval.ipynb
│   ├── 04_country_segmentation_analysis.ipynb
│   ├── 05_country_hypothesis_testing.ipynb
│   ├── 06_visualization.ipynb
│   └── 07_logistic_regression_modeling.ipynb
│
├── src/
│   ├── __init__.py
│   └── config.py                           # Path and configuration settings
│
├── figures/
│   ├── cr_bar_chart.png
│   ├── cr_bar_ci.png
│   ├── bootstrap_uplift_distribution.png
│   ├── country_cr_bar.png
│   ├── country_uplift_bar.png
│   ├── country_bootstrap_ci.png
│   └── lift_waterfall.png
│
├── paper/
│   └── survey_AB_test.pdf                  # Reference survey paper
│
└── README.md
```

---

## Data Preprocessing

To ensure the integrity of the statistical analysis, the raw data underwent several preprocessing steps.

### Mismatch Filtering

In a valid A/B test setup:

| Group | Expected Page |
|---|---|
| `control` | `old_page` |
| `treatment` | `new_page` |

Inconsistent records were removed where:

- users in the `control` group saw `new_page`
- users in the `treatment` group saw `old_page`

These records were removed because they create ambiguity between experimental assignment and actual page exposure.

### Deduplication

Duplicate `user_id` values were checked and removed so that each user contributes only one observation to the analysis.

### Data Integration

The cleaned A/B test data was merged with the country dataset using `user_id`, followed by missing-value checks.

### Timestamp Feature Engineering

The original `timestamp` column is not stored in a standard full datetime format. Values appear in a shortened time-like format such as:

```
11:48.6
01:45.2
55:06.2
```

To avoid datetime parsing errors, the `timestamp` column was kept as text and transformed into duration-based features:

| Feature | Description |
|---|---|
| `time_raw` | Original timestamp value preserved as text |
| `elapsed_minutes` | Timestamp converted into elapsed minutes |
| `time_bucket` | Grouped time interval for exploratory binning |

The `time_bucket` feature is later used as a robustness covariate in logistic regression.

---

## Conversion Rate Analysis

After preprocessing, descriptive conversion metrics were calculated.

| Metric | Value |
|---|---|
| Old Page CR | 12.03% |
| New Page CR | 11.87% |
| Absolute Lift | -0.156 percentage points |
| Relative Uplift | -1.30% |

The old page achieved a slightly higher conversion rate than the new page.

---

## Two-Proportion Z-Test

A two-proportion z-test was used to determine whether the observed difference in conversion rates was statistically significant.

| Metric | Value |
|---|---|
| Z-statistic | -1.2949 |
| P-value | 0.1953 |
| Alpha | 0.05 |
| Decision | Fail to reject H₀ |

Since the p-value is greater than 0.05, there is not enough statistical evidence to conclude that the conversion rates of the old page and new page are significantly different.

The observed drop in conversion rate is **not statistically significant**.

---

## Bootstrap Confidence Interval

To estimate the uncertainty of the observed uplift, bootstrap resampling was applied.

| Metric | Value |
|---|---|
| Simulation | 10,000 bootstrap iterations |
| Original Uplift | -1.30% |
| Mean Bootstrap Uplift | -1.29% |
| 95% Bootstrap CI | [-3.24%, +0.71%] |

The mean bootstrap uplift is negative, suggesting that the new page tends to underperform the old page in repeated resampling.

However, the **95% confidence interval crosses zero**. This means the observed negative uplift is not statistically robust.

This supports the previous two-proportion z-test conclusion that there is not enough evidence to claim a significant difference between the two pages.

---

## Country Segmentation

The analysis was broken down by country to check for localized effects.

| Country | Old Page CR | New Page CR | Relative Uplift |
|---|---|---|---|
| UK | 12.00% | 12.11% | +0.92% |
| US | 12.06% | 11.85% | -1.76% |
| CA | 11.88% | 11.18% | -5.92% |

### Country-Level Insight

- **UK** shows a small positive descriptive uplift.
- **US** shows a negative descriptive uplift and represents the largest user segment.
- **CA** shows the largest negative relative uplift.

The new page does not show consistent improvement across markets.

---

## Country-Level Statistical Testing

To verify whether the observed country-level differences were statistically significant, two-proportion z-tests were conducted separately for each country.

Across CA, UK, and US, **none of the country-level p-values fell below the 0.05 significance threshold**.

Therefore, there is not enough statistical evidence to conclude that the new page performs significantly differently from the old page within any individual country.

Bonferroni correction was also applied to account for multiple comparisons across countries.

---

## Country-Level Bootstrap Confidence Intervals

Country-level bootstrap confidence intervals were computed to estimate the uncertainty of uplift in each market.

| Country | Original Uplift | Mean Bootstrap Uplift | 95% Bootstrap CI | Contains 0 |
|---|---|---|---|---|
| CA | -5.92% | -5.82% | [-14.29%, +3.11%] | True |
| UK | +0.92% | +0.93% | [-3.00%, +4.95%] | True |
| US | -1.76% | -1.76% | [-4.09%, +0.62%] | True |

All country-level bootstrap confidence intervals contain zero.

This means that **none of the country-specific uplift estimates are statistically robust**.

### Product Risk Insight: Canada Segment

The Canadian market shows the largest negative descriptive uplift among all countries.

| Metric | Value |
|---|---|
| Original uplift | -5.92% |
| Mean bootstrap uplift | -5.82% |
| 95% Bootstrap CI | [-14.29%, +3.11%] |

Although the confidence interval contains 0, the **risk profile is asymmetric**.

- The possible upside is limited to about **+3.11%**, while the downside range extends to approximately **-14.29%**.

From a product risk perspective, this is concerning. Even though the result is not statistically significant, the potential downside in CA is too large to ignore.

This supports the recommendation **not to roll out the new page** at this stage.

---

## Visualization

Visual reporting was generated to communicate results and risks clearly.

The following figures were created and saved in the `figures/` directory:

| Figure | Description |
|---|---|
| `cr_bar_chart.png` | Basic conversion rate comparison between old page and new page |
| `cr_bar_ci.png` | Conversion rate comparison with 95% confidence intervals |
| `bootstrap_uplift_distribution.png` | Bootstrap distribution of relative uplift |
| `country_cr_bar.png` | Conversion rate comparison by country and landing page |
| `country_uplift_bar.png` | Relative uplift by country |
| `country_bootstrap_ci.png` | Country-level bootstrap confidence intervals |
| `lift_waterfall.png` | Waterfall chart showing old page CR, change, and new page CR |

---

## Logistic Regression Modeling

Logistic regression was applied as a complementary inference model because the outcome variable `converted` is binary.

The goal was not to maximize prediction accuracy, but to **estimate whether treatment assignment is associated with conversion probability** after controlling for country and time-related variation.

### Models

| Model | Formula | Purpose |
|---|---|---|
| Model 1 | `converted ~ treat` | Baseline treatment-only model |
| Model 2 | `converted ~ treat + C(country)` | Country-adjusted model |
| Model 2b | `converted ~ treat + C(country) + C(time_bucket)` | Country and time-adjusted robustness model |
| Model 3 | `converted ~ treat * C(country, Treatment(reference='US'))` | Heterogeneous treatment effect model |

### Balance Checks

After preprocessing, the treatment and control groups remained well-balanced.

| Check | Result |
|---|---|
| Sample size | Balanced |
| Country distribution | Balanced |
| Time bucket distribution | Balanced |

### Main Logistic Regression Finding

Across all logistic regression models, the treatment coefficient remained negative but statistically non-significant.

| Model | Treatment Odds Ratio | p-value | Interpretation |
|---|---|---|---|
| Basic treatment-only | 0.9852 | 0.195 | Not significant |
| Country-adjusted | 0.9853 | 0.197 | Not significant |
| Country + time adjusted | 0.9852 | 0.195 | Not significant |
| Country interaction | 0.9801 | 0.142 | Not significant |

The treatment odds ratio is consistently below 1, indicating that the new page is associated with slightly lower conversion odds.

However, the effect is **not statistically significant** in any model.

### Interaction Model

The interaction model used **US** as the reference country because it has the largest sample size.

The interaction terms for CA and UK were **not statistically significant**.

This means there is no reliable evidence that the treatment effect differs significantly across countries.

### Model Diagnostics

Model comparison showed that adding country, time bucket, and interaction terms did not substantially improve model fit.

| Diagnostic | Result |
|---|---|
| AIC / BIC | More complex models did not provide meaningful improvement |
| Pseudo R² | Extremely small across all models |
| LLR p-values | All above 0.05 |
| VIF | All variables within acceptable range |

The VIF results showed **no severe multicollinearity problem**.

Therefore, the logistic regression results support the earlier z-test, bootstrap, and country-level findings.

---

## Final Business Recommendation

Based on all statistical and modeling evidence, the recommendation is:

> **Do not roll out the new page at this stage.**

**Reasons:**

1. The new page has a slightly lower observed conversion rate.
2. The overall z-test is not statistically significant.
3. The bootstrap confidence interval contains zero.
4. No country-level result is statistically significant.
5. CA shows a large downside risk.
6. Logistic regression does not show reliable treatment improvement.
7. Country and time adjustments do not change the conclusion.
8. Interaction terms do not support targeted rollout by country.

Further redesign and additional testing are recommended before considering deployment.

---

## Current Progress

- [x] Load raw datasets
- [x] Missing value and duplicate user checks
- [x] Assignment-page mismatch filtering
- [x] Merge country information
- [x] Timestamp feature engineering
- [x] Calculate Conversion Rate, Lift, and Uplift
- [x] Run Two-Proportion Z-Test
- [x] Bootstrap Confidence Interval with 10,000 iterations
- [x] Country Segmentation Analysis
- [x] Country-Level Hypothesis Testing
- [x] Country-Level Bootstrap Confidence Intervals
- [x] Data visualizations generated with Matplotlib
- [x] Logistic Regression Modeling
- [x] Logistic Regression Diagnostics
- [x] Final Business Recommendation formulated

---

## Next Steps

- [ ] **Final Report:** Summarize the full A/B testing workflow, including preprocessing, conversion rate analysis, z-test, bootstrap confidence intervals, country-level analysis, visualization, logistic regression, and business recommendation.
- [ ] **Optional Bayesian A/B Testing:** Estimate the posterior probability that treatment outperforms control using a Beta-Binomial model.
- [ ] **Optional Business Impact Scenario Analysis:** Estimate potential conversion gain or loss under different traffic scenarios.

---

## Limitations

The current dataset does not include:

- Revenue
- Device type
- Traffic source
- Funnel steps
- Cart value
- User type
- Detailed session behavior

Therefore, the current analysis focuses on **conversion rate** rather than revenue per session, device-level effects, or funnel drop-off behavior.

Future work could be improved with richer behavioral and business features.
