import matplotlib.pyplot as plt

# Data
x = ["Jan","Feb","Mar","Apr","May"]
y = [120, 150, 170, 200, 220]   # Product sales

plt.plot(x,y)
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()