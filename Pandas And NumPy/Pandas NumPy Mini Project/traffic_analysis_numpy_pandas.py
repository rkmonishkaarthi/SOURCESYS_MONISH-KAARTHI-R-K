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

# Vehicle Contribution Percentage

percentage = (vehicle_totals / vehicle_totals.sum()) * 100

print("\nVehicle Contribution (%)")
print(percentage)

# NumPy Traffic Statistics

traffic_array = np.array(df["Total"])

print("\nTraffic Statistics (NumPy)")
print("Average Traffic:", np.mean(traffic_array))
print("Maximum Traffic:", np.max(traffic_array))
print("Minimum Traffic:", np.min(traffic_array))
print("Standard Deviation:", np.std(traffic_array))