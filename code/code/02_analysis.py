# Household Food Expenditure Project
# Regression Analysis
#
# This script estimates the main regressions from the paper.

import pandas as pd
import statsmodels.formula.api as smf
# Load cleaned data


df = pd.read_csv("data/ce_clean.csv") 
# Food at home regression
home_model = smf.ols(
    "log_food_home ~ low_income + C(year) + C(quarter)",
    data=df
).fit()


# Food away from home regression
away_model = smf.ols(
    "log_food_away ~ low_income + C(year) + C(quarter)",
    data=df
).fit()


# Print regression results
print(home_model.summary())
print(away_model.summary())
