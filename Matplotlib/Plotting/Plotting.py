import matplotlib.pyplot as plt

# Scatter Plot 
hours = [1,2,3,4,5,6]
marks = [40,50,60,70,85,90]

plt.scatter(hours,marks)
plt.xlabel("my study hours")
plt.ylabel("my marks per subject")
plt.title("scatter plot")
plt.savefig("scatterplot2.png")
plt.show()

# Bar Plot
products = ["Pen","Book","Bag","Bottle","Scale"]
sales = [100,150,80,120,60]

plt.bar(products,sales)
plt.xlabel("products")
plt.ylabel("sales")
plt.title("product sales")
plt.savefig("barplot2.png")
plt.show()

# Histogram
marks = [55,60,65,70,75,80,85,90,95,50]

plt.hist(marks)
plt.xlabel("marks")
plt.ylabel("frequency")
plt.title("Marks Distribution")
plt.savefig("histogram2.png")
plt.show()

# Pie Chart
mobiles = ["Apple","Samsung","Realme","Vivo","Oppo","Others"]
price = [50000,45000,20000,25000,30000,15000]

plt.pie(price, labels=mobiles, autopct="%1.1f%%", startangle=90)
plt.title("Share")
plt.savefig("piechart.png")
plt.axis("equal")
plt.show()