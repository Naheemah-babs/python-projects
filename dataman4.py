import pandas as pd

sales_data = {
    "Region": [
        "North", "North", "South", "South",
        "East", "East", "West", "West",
        "North", "South", "East", "West"
    ],
    "Product": [
        "Laptop", "Phone", "Laptop", "Tablet",
        "Phone", "Laptop", "Tablet", "Phone",
        "Tablet", "Phone", "Tablet", "Laptop"
    ],
    "Year": [
        2023, 2023, 2023, 2023,
        2024, 2024, 2024, 2024,
        2025, 2025, 2025, 2025
    ],
    "Sales": [
        2500, 1800, 2200, 1500,
        2000, 2700, 1600, 1900,
        2100, 2300, 1700, 2800
    ],
    "Quantity": [
        25, 30, 22, 18,
        28, 24, 20, 26,
        23, 29, 19, 27
    ]
}

df = pd.DataFrame(sales_data)

print(df)

grouped = df.groupby(["Region", "Product"])
print(grouped)

# Pivot Table (Total Sales per Region and Year)
pivot = pd.pivot_table(
    df,
    values="Sales",
    index = "Region",
    columns = "Year",
    aggfunc = "sum"
)
print(pivot)

#variance
variance = df.groupby("Region")["Sales"].var()
print(variance)

def calculate_variance(series):
    return series.var()

variance = df.groupby("Region")["Sales"].agg(calculate_variance)

print(variance)