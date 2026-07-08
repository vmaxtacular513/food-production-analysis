# responsible for line charts, bar charts, comparison charts
import pandas as pd
import matplotlib.pyplot as plt

us_maize = pd.read_csv(
    "output/reports/us_maize_by_year.csv"
)

china_maize = pd.read_csv(
    "output/reports/china_maize_by_year.csv"
)

plt.figure(figsize=(10,6))

plt.plot(
    us_maize["Year"],
    us_maize["Maize"],
    label="United States"
)

plt.plot(
    china_maize["Year"],
    china_maize["Maize"],
    label="China"
)

plt.title("US vs China Maize Production")
plt.xlabel("Year")
plt.ylabel("Production (Tonnes)")

plt.savefig(
    "output/charts/us_vs_china_maize_production.png",
    bbox_inches="tight"
)

plt.close()