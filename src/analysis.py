# Responsible for top producers, country comparisons, trend analysis, summary tables
import pandas as pd

production = pd.read_csv(
    "output/tables/clean_production.csv"
)

maize = (
    production.groupby("Country")["Maize"]
    .sum()
    .sort_values(ascending=False)
)

maize.to_csv(
    "output/reports/top_maize_producers.csv"
)

wheat = (
    production.groupby("Country")["Wheat"]
    .sum()
    .sort_values(ascending=False)
)

wheat.to_csv(
    "output/reports/top_wheat_producers.csv"
)

rice = (
    production.groupby("Country")["Rice"]
    .sum()
    .sort_values(ascending=False)
)

rice.to_csv(
    "output/reports/top_rice_producers.csv"
)

usa = production[
    production["Country"] == "United States"             
]

us_maize = usa[
    ["Year", "Maize"]
]

us_maize = us_maize.sort_values(
    by="Year"
)

us_maize.to_csv(
    "output/reports/us_maize_by_year.csv"
)

us_wheat = usa[
    ["Year", "Wheat"]
]

us_wheat = us_wheat.sort_values(
    by="Year"
)

us_wheat.to_csv(
    "output/reports/us_wheat_by_year.csv"
)

us_rice = usa[
    ["Year", "Rice"]
    ]

us_rice = us_rice.sort_values(
    by="Year"
)

us_rice.to_csv(
    "output/reports/us_rice_by_year.csv"
)

china = production[
    production["Country"] == "China"             
]

china_maize = china[
    ["Year", "Maize"]
]

china_maize = china_maize.sort_values(
    by="Year"
)

china_maize.to_csv(
    "output/reports/china_maize_by_year.csv"
)

china_wheat = china[
    ["Year", "Wheat"]
]

china_wheat = china_wheat.sort_values(
    by="Year"
)

china_wheat.to_csv(
    "output/reports/china_wheat_by_year.csv"
)

china_rice = china[
    ["Year", "Rice"]
]

china_rice = china_rice.sort_values(
    by="Year"
)

china_rice.to_csv(
    "output/reports/china_rice_by_year.csv"
)

# ENTITY INVESTIGATION

countries = production["Country"].unique()

# for item in sorted(countries):
#    print(item)

# ------------------------------
# COUNTRY FILTER
# ------------------------------

aggregate_entities = [
    "World",
    "Africa",
    "Asia",
    "Europe",
    "North America",
    "South America",
    "Oceania",
    "Melanesia",
    "High-income countries",
    "Upper-middle-income countries",
    "Lower-middle-income countries",
    "Low-income countries",
    "European Union (27)"
]

countries_only = production[
    ~production["Country"].str.contains(
        r"\(FAO\)",
        regex=True
    )
]

countries_only = countries_only[
    ~countries_only["Country"].isin(
        aggregate_entities
    )
]

    
maize_country = (
    countries_only.groupby("Country")
    ["Maize"]
    .sum()
    .sort_values(ascending=False)
)

maize_country.to_csv(
    "output/reports/top_maize_producers_countries_only.csv"
)

rice_country = (
    countries_only.groupby("Country")
    ["Rice"]
    .sum()
    .sort_values(ascending=False)
)

rice_country.to_csv(
    "output/reports/top_rice_producers_countries_only.csv"
)

wheat_country = (
    countries_only.groupby("Country")
    ["Wheat"]
    .sum()
    .sort_values(ascending=False)
)

wheat_country.to_csv(
    "output/reports/top_wheat_producers_countries_only.csv"
)

saint_lucia = countries_only[
    countries_only["Country"] == "Saint Lucia"
]

production["Wheat"].describe()

wheat_large = (
    countries_only[
        ["Country", "Year", "Wheat"]
    ]
    .sort_values(
        by="Wheat",
        ascending=False
    )
)

china = countries_only[
    countries_only["Country"] == "China"
]

south_africa = countries_only[
    countries_only["Country"] == "South Africa"
]

for country in [
    "China",
    "India",
    "Vietnam",
    "Thailand"
]:
    total = countries_only[
        countries_only["Country"] == country
    ]["Rice"].sum()

    print(country, total)

china = countries_only[
    countries_only["Country"] == "China"
]

print(
    china[
        ["Year", "Rice"]
        ]
)