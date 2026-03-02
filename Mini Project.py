import numpy as np

np.random.seed(42)

# 600 employees, 10 months sales
sales = np.random.randint(0, 100, size=(600, 10))
print("Sales Data:\n", sales)

avg = np.mean(sales,axis=1)
print("\nAvg Sales per Employee:\n",avg)

month_avg = np.mean(sales, axis=0)
print("\nAvg Sales per Month:\n", month_avg)

best_employee = np.argmax(avg)
print("\nBest Employee :", best_employee)

employee_std = np.std(sales, axis=1)
print("\nEmployee Sales Std:\n", employee_std)

low = np.where(avg < 40)
print("\nEmployees Below Target:\n", low)

ranking = np.argsort(avg)
top3 = ranking[:3]
print("\nTop 3 Employees:\n", top3)

weights = np.array([0.05, 0.05, 0.08, 0.1, 0.12, 0.1, 0.1, 0.15, 0.15, 0.1])
weighted_performance = np.dot(sales, weights)
print("\nWeighted Performance:\n", weighted_performance)

