# 7/7/2026

## What I learned

- Loading CSV files with Pandas
- Cleaning column names
- Creating analysis tables
- Creating line charts with Matplotlib
- Saving outputs
- Using Git and Github

## Challenges

- Inconsistent column names
- Wheat production anomalies
- Relearning Git

## Questions

- Why are some wheat values unusual?
- How can I compare more countries?
- How should I structure future projects?

# 7/8/2026

## Data Quality Observations

The dataset includes both countries and aggregate entities

Examples:
- Africa 
- Africa (FAO)
- Asia
- Asia (FAO)
- Northern America
- Northern America (FAO)

These aggregate regions may distort rankings if included alongside individual countries. Future analysis may require filtering out regional aggregates.

## Questions

- What entities in this dataset are true countries versus aggregate groups?
Why it matters:
Aggregate regions distort country rankings and can lead to misleading conclusions.

- What are the top 10 maize-producing countries, and what share of total production do they represent?

## Today's Insight

Initial rankings were dominated by aggregate entities such as World, Asia, and North America.

Filtering out FAO regions and economic groups are more meaningful country-level analysis. 

These entities distorted country rankings.

### Action Taken

Created a filtered dataset for country-level maize production rankings. 

### Result

Country rankings now better reflect actual national production levels.