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

plt.figure(figsize=(10,5))

plt.plot(data["Date"], data["Subways"], label="Subways")
plt.plot(data["Date"], data["Buses"], label="Buses")

plt.title("Public Transport Ridership Trend")
plt.xlabel("Date")
plt.ylabel("Passengers")
plt.legend()
plt.grid(True)

plt.xticks(rotation=45)

max_value = data["Subways"].max()
max_index = data["Subways"].idxmax()
max_date = data["Date"][max_index]

plt.annotate(
    "Highest Subway Ridership",
    xy=(max_date, max_value),
    xytext=(max_date, max_value + 200000),
    arrowprops=dict(facecolor='black')
)
plt.show()

transport = ["Subways", "Buses", "LIRR", "MetroNorth"]
avg_values = [avg_subway, avg_bus, avg_lirr, avg_metro]

plt.figure(figsize=(6,4))

plt.bar(transport, avg_values)

plt.title("Average Transport Ridership")
plt.xlabel("Transport Type")
plt.ylabel("Average Passengers")

plt.grid(True)

plt.show()


plt.figure(figsize=(6,4))

plt.scatter(data["Buses"], data["Subways"])

plt.title("Bus vs Subway Ridership")
plt.xlabel("Bus Passengers")
plt.ylabel("Subway Passengers")

plt.grid(True)

plt.show()

# Subplots
fig, ax = plt.subplots(2, 2, figsize=(12,8))

ax[0,0].plot(data["Date"], data["Subways"], label="Subways")
ax[0,0].plot(data["Date"], data["Buses"], label="Buses")
ax[0,0].set_title("Transport Ridership Trend")
ax[0,0].legend()
ax[0,0].grid(True)

transport = ["Subways","Buses","LIRR","MetroNorth"]
avg_values = [avg_subway, avg_bus, avg_lirr, avg_metro]

ax[0,1].bar(transport, avg_values)
ax[0,1].set_title("Average Ridership")
ax[0,1].grid(True)

ax[1,0].scatter(data["Buses"], data["Subways"])
ax[1,0].set_title("Bus vs Subway Ridership")
ax[1,0].grid(True)

ax[1,1].plot(data["Date"], data["LIRR"], label="LIRR")
ax[1,1].plot(data["Date"], data["MetroNorth"], label="MetroNorth")
ax[1,1].set_title("Rail Ridership Trend")
ax[1,1].legend()
ax[1,1].grid(True)

plt.tight_layout()

plt.savefig("transport_subplots.png")

plt.show()