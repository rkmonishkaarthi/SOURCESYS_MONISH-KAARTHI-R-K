import matplotlib.pyplot as plt

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

temperature = [30,32,31,29,28,27,26]
humidity = [65,70,68,72,75,80,78]
rainfall = [5,0,10,20,15,25,30]

fig, ax = plt.subplots(2,2, figsize=(10,8))

# Temperature line chart
ax[0,0].plot(days, temperature, marker='o', color='red', label="Temperature")
ax[0,0].set_title("Temperature Trend")
ax[0,0].set_xlabel("Days")
ax[0,0].set_ylabel("Temperature (°C)")
ax[0,0].legend()
ax[0,0].grid(True)

# Annotate highest temperature
max_temp = max(temperature)
max_day = days[temperature.index(max_temp)]

ax[0,0].annotate(
    "Highest Temp",
    xy=(max_day, max_temp),
    xytext=(max_day, max_temp+2),
    arrowprops=dict(facecolor='black')
)

# Rainfall bar chart
ax[0,1].bar(days, rainfall, color='blue', label="Rainfall")
ax[0,1].set_title("Rainfall per Day")
ax[0,1].set_xlabel("Days")
ax[0,1].set_ylabel("Rainfall (mm)")
ax[0,1].legend()
ax[0,1].grid(True)

# Annotate highest rainfall
max_rain = max(rainfall)
max_rain_day = days[rainfall.index(max_rain)]

ax[0,1].annotate(
    "Heavy Rain",
    xy=(max_rain_day, max_rain),
    xytext=(max_rain_day, max_rain+5),
    arrowprops=dict(facecolor='blue')
)

# Scatter plot
ax[1,0].scatter(temperature, humidity, color='green', label="Temp vs Humidity")
ax[1,0].set_title("Temperature vs Humidity")
ax[1,0].set_xlabel("Temperature")
ax[1,0].set_ylabel("Humidity")
ax[1,0].legend()
ax[1,0].grid(True)

# Histogram
ax[1,1].hist(temperature, bins=5, color='orange', label="Temp Distribution")
ax[1,1].set_title("Temperature Distribution")
ax[1,1].set_xlabel("Temperature")
ax[1,1].set_ylabel("Frequency")
ax[1,1].legend()
ax[1,1].grid(True)

# Dashboard title
fig.suptitle("Weather Data Visualization Dashboard", fontsize=16)

plt.tight_layout()
plt.savefig("weather_dashboard.png")
plt.show()