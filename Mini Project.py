import numpy as np

np.random.seed(42)

# 100 employees, 5 months sales
sales = np.random.randint(0, 100, size=(600, 10))

print("Sales Data:\n", sales)
avg = np.mean(sales,axis=1)

print("\nAvg Sales per Employee:\n",avg)