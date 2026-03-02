import numpy as np

np.random.seed(42)

# 600 employees, 10 months sales
sales = np.random.randint(0, 100, size=(600, 10))
print("Sales Data:\n", sales)

avg = np.mean(sales,axis=1)
print("\nAvg Sales per Employee:\n",avg)

month_avg = np.mean(sales, axis=0)
print("\nAvg Sales per Month:\n", month_avg)

best_employee = np.argmax(employee_avg)
print("\nBest Employee :", best_employee)

employee_std = np.std(sales, axis=1)
print("\nEmployee Sales Std:\n", employee_std)

low = np.where(employee_avg < 40)
print("\nEmployees Below Target:\n", low)

ranking = np.argsort(employee_avg)
top3 = ranking[-3:]
print("\nTop 3 Employees:\n", top3)
