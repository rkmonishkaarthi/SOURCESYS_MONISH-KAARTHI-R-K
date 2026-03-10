import matplotlib.pyplot as plt

# Data
x = ["Jan","Feb","Mar","Apr","May"]
y1 = [120, 150, 170, 200, 220]   # Product A sales
y2 = [100, 130, 160, 180, 210]   # Product B sales
plt.figure(figsize=(10,5),dpi=100)
plt.plot(x, y1, color="blue", linestyle="--", linewidth=2, marker="s", markersize=6,label='Product A')
plt.plot(x, y2, color="orange", linestyle="dotted", linewidth=2, marker="d", markersize=6,label='Product B')

plt.annotate(
    "Highest",
    xy=("May",220),
    xytext=("Apr",190),
    arrowprops=dict(facecolor="green")
)

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales Graph")
plt.legend()
# plt.savefig("salesplot.png")
plt.savefig("salesplot.jpg")
plt.grid(True)
plt.show()