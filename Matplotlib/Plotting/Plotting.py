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

# # Bar Plot
# products = ["A","B","C","D","E"]
# sales = [70,50,40,90,30]

# plt.bar(products,sales)
# plt.xlabel("products")
# plt.ylabel("sales")
# plt.title("product sales")
# plt.savefig("barplot1.png")
# plt.show()

# Histogram
# marks = [60,42,67,78,89,92,45,32,42,83,85]

# plt.hist(marks)
# plt.xlabel("marks")
# plt.ylabel("frequency")
# plt.title("Marks Distribution")
# plt.savefig("histogram.png")
# plt.show()

# Pie Chart
mobiles = ["Apple","Samsung","Realme","Vivo","Oppo","Others"]
price = [60000,40000,25000,28000,32000,70000]

plt.pie(price, labels=mobiles, autopct="%1.1f%%", startangle=90)
plt.title("Share")
plt.savefig("piechart.png")
plt.axis("equal")
plt.show()