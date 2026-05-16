#  A/B Testing Analysis for Checkout Page Design

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-150458.svg)
![Statsmodels](https://img.shields.io/badge/Statsmodels-Statistical_Modeling-green.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange.svg)

## Project Overview
In e-commerce, the checkout page is a critical touchpoint. Even minor design modifications can significantly impact whether users complete a purchase or abandon their carts.

This repository contains an end-to-end A/B testing analysis to evaluate whether a newly redesigned checkout page (`new_page`) improves the conversion rate compared to the existing design (`old_page`).

**Final Business Recommendation:** Do not roll out the new page at this stage. The new design does not show statistically significant improvement in conversion rate, and the observed uplift is slightly negative. Further design iteration and additional testing are recommended before any full rollout decision.

---

## Research Problem
The core objective is to determine if the difference in conversion rates between the old and new pages is statistically significant, or merely due to random chance.

We formulated a two-tailed hypothesis test:
* **Null Hypothesis (H0):** The new checkout page has the exact same conversion rate as the old page (`CR_new = CR_old`).
* **Alternative Hypothesis (H1):** The new checkout page has a different conversion rate compared to the old page (`CR_new != CR_old`).

---

## Dataset
The analysis is based on two raw datasets:
1. `ab_test.csv`: Contains user interactions during the test period.
   * `user_id`: Unique identifier for each user.
   * `timestamp`: Time of the visit.
   * `group`: A/B test assignment (`control` or `treatment`).
   * `landing_page`: The page actually seen (`old_page` or `new_page`).
   * `converted`: Binary outcome (`1` = purchased, `0` = did not purchase).
2. `countries_ab.csv`: Maps each `user_id` to their respective `country` (US, UK, CA).

---

## Repository Structure

```
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
│       ├── ztest_results.csv
│       ├── bootstrap_results.csv
│       ├── bootstrap_summary.csv
│       ├── country_summary.csv
│       ├── country_uplift.csv
│       ├── country_ztest_results.csv
│       ├── country_bootstrap_summary.csv
│       └── country_final_results.csv
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_conversion_rate_ab_test.ipynb
│   ├── 03_bootstrap_confidence_interval.ipynb
│   ├── 04_country_segmentation_analysis.ipynb
│   ├── 05_country_hypothesis_testing.ipynb
│   └── 06_visualization.ipynb
│
├── src/
│   ├── __init__.py
│   └── config.py
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
├── reports/
│
├── README.md
├── requirements.txt
├── .gitignore
└── main.py
```

---

## Data Preprocessing
To ensure the integrity of the statistical analysis, the raw data underwent rigorous cleaning:
* **Mismatch Filtering:** Removed inconsistent records where users in the `control` group were mistakenly served the `new_page`, and users in the `treatment` group saw the `old_page`.
* **Deduplication:** Checked and removed duplicate `user_id`s so that each user is counted exactly once.
* **Data Integration:** Merged the cleaned A/B test data with the country dataset using a left join on `user_id`, followed by missing-value checks.
* **Timestamp Feature Engineering:** The original `timestamp` column is not stored in a standard full datetime format — values appear in a shortened time-like format such as `11:48.6`, `01:45.2`, and `55:06.2`. To avoid datetime parsing errors, the column is kept as text and transformed into the following duration-based features:
  * `time_raw`: the original timestamp value preserved as text.
  * `elapsed_minutes`: the timestamp converted into elapsed minutes as a numeric value.
  * `time_bucket`: a grouped time interval for exploratory binning.

---

## Conversion Rate Analysis
After preprocessing, we calculated the descriptive performance metrics and ran a Frequentist statistical test.

* **Old Page (Control) CR:** 12.03%
* **New Page (Treatment) CR:** 11.87%
* **Absolute Lift:** -0.156 percentage points
* **Relative Uplift:** -1.30%

**Two-Proportion Z-Test Results:**
* **Z-Statistic:** -1.2949
* **P-Value:** 0.1953 (Alpha = 0.05)
* **Conclusion:** Since P-value > 0.05, we **fail to reject the Null Hypothesis**. The observed drop in conversion rate is not statistically significant.

---

## Bootstrap
To further estimate the uncertainty of the observed uplift, a bootstrap resampling method was applied.

* **Simulation:** 10,000 iterations of sampling with replacement.
* **Original Uplift:** -1.30%
* **Mean Bootstrap Uplift:** -1.29%
* **95% Confidence Interval (CI):** `[-3.24%, +0.71%]`

**Insight:** The mean bootstrap uplift is negative, suggesting that the new page tends to underperform the old page in repeated resampling. However, the 95% confidence interval crosses zero, meaning the observed negative uplift is not statistically robust. This supports the previous two-proportion z-test conclusion that there is not enough evidence to claim a significant difference between the two pages.

---

## Country Segmentation
We broke down the performance by market to check for localized effects:

| Country | Old Page CR | New Page CR | Relative Uplift |
| :--- | :--- | :--- | :--- |
| **UK** | 12.00% | 12.11% | +0.92% |
| **US** | 12.06% | 11.85% | -1.76% |
| **CA** | 11.88% | 11.18% | -5.92% |

**Insight (Market-Level Risk):** While the UK showed a slight positive trend, both the US and CA segments showed negative uplift. CA had the largest relative decline (-5.92%), while the US segment had the largest user base and therefore strongly influenced the overall result. This indicates that the new design does not deliver consistent improvement across markets.

---

## Country-Level Statistical Testing

To verify whether the observed country-level differences were statistically significant, two-proportion z-tests were conducted separately for each country.

Across CA, UK, and US, none of the country-level p-values fell below the 0.05 significance threshold. Therefore, there is not enough statistical evidence to conclude that the new page performs significantly differently from the old page within any individual country.

Country-level bootstrap confidence intervals were also computed to estimate the uncertainty of uplift in each market. These results further support the conclusion that the observed country-level differences should be interpreted cautiously.

### Product Risk Insight: Canada Segment

The Canadian market shows the largest negative descriptive uplift among all countries.

| Metric | Value |
| :--- | ---: |
| Original uplift | -5.92% |
| Mean bootstrap uplift | -5.82% |
| 95% Bootstrap CI | [-14.29%, +3.11%] |

Although the confidence interval contains 0, the risk profile is asymmetric. The possible upside is limited (+3.11%), while the downside range is nearly 4.6× larger (-14.29%). In the best-case scenario, the new page may improve conversion by around 3.11%, but in the worst-case scenario, it may reduce conversion by as much as 14.29%.

From a product risk perspective, this is concerning. Even though the result is not statistically significant, the potential downside in CA is too large to ignore. This supports the overall recommendation not to roll out the new page at this stage.

### Business Risk Interpretation

Although the country-level results are not statistically significant under the traditional frequentist threshold, the bootstrap confidence intervals provide an important business risk perspective.

Product decisions should not rely only on whether a confidence interval crosses zero. From a risk management perspective, the size and direction of potential downside outcomes also matter. In this case:

- **UK** shows a small positive descriptive uplift.
- **US** shows a negative descriptive uplift and represents the largest user segment, strongly influencing the overall result.
- **CA** shows the largest negative relative uplift and the widest downside risk.

Therefore, even though the statistical tests do not prove that the new page is significantly worse, the risk profile does not support a full rollout.

> **Recommendation:** Do not roll out the new page at this stage. Further redesign and additional testing are recommended before considering deployment.

---

## Visualization
Visual reporting was generated to communicate risks to stakeholders clearly. *(Charts are available in the `figures/` directory).*

1. **Conversion Rate Bar Chart with CI:** (`cr_bar_ci.png`) Shows the overlapping error bars, visualizing the lack of statistical significance.
2. **Bootstrap Uplift Distribution:** (`bootstrap_uplift_distribution.png`) A histogram showing that the majority of simulated outcomes fall below the 0% threshold.
3. **Country Uplift Bar Chart:** (`country_uplift_bar.png`) Highlights the severe underperformance in the CA market.
4. **Lift Waterfall Chart:** (`lift_waterfall.png`) A business-friendly chart demonstrating the absolute drop from 12.03% to 11.87%.

---

## Current Progress
- [x] Load raw datasets
- [x] Missing value & duplicate user checks
- [x] Assignment-page mismatch filtering
- [x] Merge country information
- [x] Timestamp feature engineering (`time_raw`, `elapsed_minutes`, `time_bucket`)
- [x] Calculate descriptive Conversion Rates & Lifts
- [x] Run Two-Proportion Z-Test
- [x] Bootstrap Confidence Interval (10,000 iterations)
- [x] Country Segmentation analysis
- [x] Country-Level Hypothesis Testing
- [x] Country-Level Bootstrap Confidence Intervals
- [x] Data visualizations generated with Matplotlib
- [x] Final Business Recommendation formulated

---

## Next Steps

- [ ] **Logistic Regression Modeling:** Build models such as `converted ~ new_page`, `converted ~ new_page + country`, and `converted ~ new_page * country` to evaluate whether the page effect remains after controlling for country and whether the treatment effect varies across country segments.

- [ ] **Final Report:** Summarize the full A/B testing workflow, including preprocessing, conversion rate analysis, z-test, bootstrap confidence intervals, country-level analysis, visualization, and business recommendation.

- [ ] **Time-Based Exploratory Analysis:** The `timestamp` column has been transformed into duration-based features (`elapsed_minutes`, `time_bucket`). These features can be used to explore whether conversion behavior varies across different time intervals within the test period (e.g., novelty effects or time-of-day patterns). Full time-series analysis is not applicable because the original `timestamp` is not stored in a standard datetime format.
