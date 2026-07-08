import pandas as pd

# Responsible for read csv, clean columns, rename fields, validate data
production = pd.read_csv("data/food_production.csv")

production.columns = (
    production.columns
    .str.strip()
    .str.replace(r"\s+", "_", regex=True)
) 

production = production.rename(columns={
    "Entity": "Country",
    "Maize_Production_(tonnes)": "Maize",
    "Rice_Production_(_tonnes)": "Rice",
    "Yams_Production_(tonnes)": "Yams",
    "Wheat_Production_(tonnes)": "Wheat",
    "Tomatoes_Production_(tonnes)": "Tomatoes",
    "Tea_Production_(_tonnes_)": "Tea",
    "Sweet_potatoes_Production_(tonnes)": "Sweet_Potatoes",
    "Sunflower_seed_Production_(tonnes)": "Sunflower_Seed",
    "Sugar_cane_Production_(tonnes)": "Sugar_Cane",
    "Soybeans_Production_(tonnes)": "Soybeans",
    "Rye_Production_(tonnes)": "Rye",
    "Potatoes_Production_(tonnes)": "Potatoes",
    "Oranges_Production_(tonnes)": "Oranges",
    "Peas,_dry_Production_(_tonnes)": "Peas",
    "Palm_oil_Production_(tonnes)": "Palm_Oil",
    "Grapes_Production_(tonnes)": "Grapes",
    "Coffee,_green_Production_(_tonnes)": "Coffee",
    "Cocoa_beans_Production_(tonnes)": "Cocoa_Beans",
    "Meat,_chicken_Production_(tonnes)": "Chicken",
    "Bananas_Production_(_tonnes)": "Bananas",
    "Avocados_Production_(tonnes)": "Avocados",
    "Apples_Production_(tonnes)": "Apples"
})

production.to_csv(
    "output/tables/clean_production.csv",
    index=False
)

print("Clean dataset saved")