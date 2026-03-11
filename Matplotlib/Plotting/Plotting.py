import matplotlib.pyplot as plt

# Scatter Plot 
hours = [1,2,3,4,5,6]
marks = [500,700,900,1100,1300,1500]

plt.scatter(hours,marks)
plt.xlabel("my study hours")
plt.ylabel("my marks per subject")
plt.title("scatter plot")
plt.savefig("scatterplot4.png")
plt.show()

# Bar Plot
products = ["Laptop","Mouse","Keyboard","Monitor","Speaker"]
sales = [200,500,350,150,250]

plt.bar(products,sales)
plt.xlabel("products")
plt.ylabel("sales")
plt.title("product sales")
plt.savefig("barplot4.png")
plt.show()

# Histogram
marks = [450,500,600,700,800,900,1000,1100]

plt.hist(marks)
plt.xlabel("marks")
plt.ylabel("frequency")
plt.title("Marks Distribution")
plt.savefig("histogram4.png")
plt.show()

# Pie Chart
mobiles = ["North","South","East","West","Online","Retail"]
price = [30,20,15,10,15,10]

plt.pie(price, labels=mobiles, autopct="%1.1f%%", startangle=90)
plt.title("Share")
plt.savefig("piechart4.png")
plt.axis("equal")
plt.show()