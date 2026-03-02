import numpy as np

np.random.seed(42)

# 100 employees, 5 months sales
sales = np.random.randint(0, 100, size=(100, 5))

print("Sales Data:\n", sales)