# Household Food Expenditure Project
# Data Cleaning
#
# This script prepares Consumer Expenditure Survey data
# for the empirical analysis.

import pandas as pd
import numpy as np

# Load the Consumer Expenditure Survey data
df = pd.read_csv("data/ce_interview.csv")
# Expected variables:
# FINCBTXM  = total household income
# FDHOMEPQ  = food at home expenditures
# FDAWAYPQ  = food away from home expenditures
# year      = interview year
# quarter   = interview quarter

# Remove households with non-positive income
df = df[df["FINCBTXM"] > 0].copy()

# Calculate the median household income within each year
df["income_median"] = df.groupby("year")["FINCBTXM"].transform("median")

# Create low-income indicator
# 1 = below yearly median, 0 = at or above yearly median
df["low_income"] = (df["FINCBTXM"] < df["income_median"]).astype(int)


# Create log expenditure variables
df["log_food_home"] = np.log1p(df["FDHOMEPQ"])
df["log_food_away"] = np.log1p(df["FDAWAYPQ"])


# Save cleaned dataset for analysis
df.to_csv("data/ce_clean.csv", index=False)
