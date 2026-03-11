import matplotlib.pyplot as plt

# Scatter Plot 
# hours = [3,2,4,1,2,5]
# marks = [75,60,80,35,40,90]

# plt.scatter(hours,marks)
# plt.xlabel("my study hours")
# plt.ylabel("my marks per subject")
# plt.title("scatter plot")
# plt.savefig("scatterplot1.png")
# plt.show()

# Bar Plot
products = ["A","B","C","D","E"]
sales = [70,50,40,90,30]

plt.bar(products,sales)
plt.xlabel("products")
plt.ylabel("sales")
plt.title("product sales")
plt.savefig("barplot1.png")
plt.show()