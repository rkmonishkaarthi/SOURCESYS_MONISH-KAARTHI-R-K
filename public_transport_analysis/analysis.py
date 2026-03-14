import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("MTA.csv")

print("Original Dataset")
print(data.head())

# Data cleaning
data = data[[
    "Date",
    "Subways: Total Estimated Ridership",
    "Buses: Total Estimated Ridership",
    "LIRR: Total Estimated Ridership",
    "Metro-North: Total Estimated Ridership"
]]

data.columns = ["Date", "Subways", "Buses", "LIRR", "MetroNorth"]

data["Date"] = pd.to_datetime(data["Date"])

data = data.dropna()

data = data.head(50)

print("\nCleaned Dataset")
print(data.head())