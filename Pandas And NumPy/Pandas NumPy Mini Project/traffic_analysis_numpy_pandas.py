import pandas as pd
import numpy as np

df = pd.read_csv("traffictwomonth.csv")

print("\nDataset Preview")
print(df.head())

# Data Cleaning

df["Total"] = df[["CarCount", "BikeCount", "BusCount", "TruckCount"]].sum(axis=1)

df["Time"] = pd.to_datetime(df["Time"], format="%I:%M:%S %p")

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

# Peak Traffic Hour

hourly_traffic = df.groupby("Hour")["Total"].mean()

print("\nAverage Traffic Per Hour")
print(hourly_traffic)

print("\nPeak Traffic Hour:", hourly_traffic.idxmax())

# Day-wise Traffic Analysis

day_traffic = df.groupby("Day of the week")["Total"].sum()

print("\nTraffic by Day")
print(day_traffic)

print("\nMost Busy Day:", day_traffic.idxmax())

# Traffic Density Score
# weights for vehicles
weights = np.array([1, 0.5, 2, 2.5])

vehicle_matrix = df[vehicle_cols].values

density_score = np.dot(vehicle_matrix, weights)

df["Traffic Density Score"] = density_score

print("\nDataset with Traffic Density Score")
print(df.head())

# Congestion Index

df["Congestion_Index"] = df["Total"] / df["Total"].max()

print("\nCongestion Index Sample")
print(df[["Total","Congestion_Index"]].head())

# Traffic Outlier Detection

mean = np.mean(df["Total"])
std = np.std(df["Total"])

outliers = df[df["Total"] > mean + 2 * std]

print("\nTraffic Outliers")
print(outliers)

# Car/Bike Ratio

car_array = np.array(df["CarCount"])
bike_array = np.array(df["BikeCount"])

ratio = np.mean(car_array / (bike_array + 1))

print("\nAverage Car/Bike Ratio:", ratio)

# Simple Traffic Prediction

conditions = [
    df["Total"] < 20,
    df["Total"] < 50,
    df["Total"] >= 50
]

choices = ["Low","Moderate","Heavy"]

df["Predicted_Traffic"] = np.select(conditions, choices, default="Unknown")

print("\nPredicted vs Actual Traffic")
print(df[["Total","Traffic Situation","Predicted_Traffic"]].head())
