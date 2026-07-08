# Commodity Validation Report

## Objective

Evaluate whether commodity production fields can be used for country-level analysis.

## Method

1. Remove aggregate entities.
2. Rank countries by cumulative production.
3. Compare results for plausibility.

## Findings

The dataset contains:
- Countries
- Regions
- FAO aggregates
- Income classifications

Country-level analysis required filtering.

---

### Wheat

Observed extremely large values for Saint Lucia.

Large structural break occurs around 2012.

Status: Under review

---

### Rice

China appears substantially smaller than other major producers.

Country-level values may exist on inconsistent scales.

Status: Under review

---

### Maize

Country rankings appear plausible after filtering aggregate entities.

Status: Suitable for analysis


### Soybeans

Country rankings did not align with expected major producers.

Status: Requires validation.

### Potatoes

Country rankings produced potentially unreliable results.

Status: Requires validation

# Conclusion

The original goal of this project was to analyze global food production trends and identify the largest producing countries for major commodities.

During the investigation, multiple data quality issues were identified. The dataset contained a mixture of countries, regional aggregates, income classifications, and FAO statistical groupings. These entities initially distorted country-level rankings and required additional filtering.

After filtering aggregate entities, maize production rankings appeared plausible and suitable for exploratory analysis. However, wheat, rice, soybean, and potato rankings produced unexpected results that failed basic reasonableness checks. Further investigation revealed structural breaks, unusual scaling differences, and country rankings that require additional validation before reliable conclusions can be drawn.

The most important outcome of this project was not identifying the largest food producers, but learning the importance of validating datasets before accepting analytical results. This project demonstrates that data cleaning and validation are critical steps in the analytical process and that reported results should always be tested for plausibility before being used for decision-making.

Future work should focus on validating the original data sources, investigating commodity-specific methodology differences, and supplementing this dataset with higher-quality food production and food price data.