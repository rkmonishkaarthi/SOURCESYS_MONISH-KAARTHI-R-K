import matplotlib.pyplot as plt
fig, ax = plt.subplots()

x = ["Jan","Feb","Mar","Apr","May"]
y = [120, 150, 170, 200, 220]

ax.plot(x, y)

ax.set_title("subplot")
ax.set_xlabel("x_values")
ax.set_ylabel("y_values")

ax.legend(["legend"])

plt.show()