# Findings

## Data Overview

Dataset covers food production from 1961-2021.

No missing values were identified.

## Maize



### Entity Classification Issue

The dataset contains a mixture of:

- Countries
- Geographical regions
- FAO (Food Agricultural Organization) statistical regions
- Income classifications

Examples include:

- United States
- Asia
- Asia (FAO)
- High-income countries
- Americas (FAO)

These aggregate entities can distort country-level rankings and may need to be filtered out in future analyses.

### Entity Filtering

The original rankings included regional and economic aggregates such as:

- World
- North America
- Asia
- High-Income countries
- European Union (27)

A filtered version was created to better represent country-level production rankings. 

### Data Validation

Initial producer rankings contained regional, economic, and FAO aggregate entities. 

After filtering aggregate groups, country-level rankings showed the United States and China as the largest maize producers in the dataset.

The filtering process also identified additional non-country entities such as the European Union (27), demonstrating the importance of validating entity definitions before drawing conclusions.

