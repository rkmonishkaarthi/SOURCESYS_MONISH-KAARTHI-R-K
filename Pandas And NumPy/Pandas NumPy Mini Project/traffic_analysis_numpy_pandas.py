import pandas as pd
import numpy as np

df = pd.read_csv("traffictwomonth.csv")

print("\nDataset Preview")
print(df.head())

# Data Cleaning

df["Total"] = df[["CarCount", "BikeCount", "BusCount", "TruckCount"]].sum(axis=1)

df["Time"] = pd.to_datetime(df["Time"])

df["Hour"] = df["Time"].dt.hour

print("\nDataset After Cleaning")
print(df.head())

# Vehicle Distribution
vehicle_cols = ["CarCount","BikeCount","BusCount","TruckCount"]

vehicle_totals = df[vehicle_cols].sum()

print("\nVehicle Distribution")
print(vehicle_totals)