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

avg_subway = np.mean(data["Subways"])
avg_bus = np.mean(data["Buses"])
avg_lirr = np.mean(data["LIRR"])
avg_metro = np.mean(data["MetroNorth"])

total_subway = np.sum(data["Subways"])
total_bus = np.sum(data["Buses"])

print("\nAverage Subway Ridership:", avg_subway)
print("Average Bus Ridership:", avg_bus)
print("Average LIRR Ridership:", avg_lirr)
print("Average MetroNorth Ridership:", avg_metro)

print("\nTotal Subway Ridership:", total_subway)
print("Total Bus Ridership:", total_bus)