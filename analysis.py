"""
Car Market Trends Analysis with Car Dekho Data
Student: MEESALA CHINNA REDDAIAH
AICTE STU ID: STU6a5fa4510cde41784652881
"""

import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "1776311302-P3-Car Market Trends Analysis with Car Dekho Data.csv"

df = pd.read_csv(DATA_FILE)

# Basic data quality checks
print("Shape:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# Remove duplicate rows
data = df.drop_duplicates().copy()

# Derived fields
# The supplied dataset ends at 2018, so 2018 is used as the dataset reference year.
data["Car_Age"] = 2018 - data["Year"]
data["Depreciation"] = data["Present_Price"] - data["Selling_Price"]
data["Resale_Percentage"] = data["Selling_Price"] / data["Present_Price"] * 100

print("\nAverage selling price:", round(data["Selling_Price"].mean(), 2), "lakh")
print("Median selling price:", round(data["Selling_Price"].median(), 2), "lakh")
print("Average present price:", round(data["Present_Price"].mean(), 2), "lakh")

print("\nAverage selling price by fuel type:")
print(data.groupby("Fuel_Type")["Selling_Price"].mean().sort_values(ascending=False))

print("\nAverage selling price by seller type:")
print(data.groupby("Seller_Type")["Selling_Price"].mean().sort_values(ascending=False))

print("\nAverage selling price by transmission:")
print(data.groupby("Transmission")["Selling_Price"].mean().sort_values(ascending=False))

print("\nCorrelation with selling price:")
print(data[["Year", "Selling_Price", "Present_Price", "Kms_Driven", "Owner"]].corr()["Selling_Price"].sort_values(ascending=False))

# Example chart
data.groupby("Year")["Selling_Price"].mean().plot(marker="o", figsize=(8, 4.5))
plt.title("Average Selling Price by Manufacturing Year")
plt.xlabel("Manufacturing Year")
plt.ylabel("Average Selling Price (₹ lakh)")
plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()
