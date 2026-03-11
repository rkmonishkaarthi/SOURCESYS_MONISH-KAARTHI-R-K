import matplotlib.pyplot as plt

# Scatter Plot 
hours = [1,2,3,4,5,6]
marks = [200,300,350,420,480,520]

plt.scatter(hours,marks)
plt.xlabel("my study hours")
plt.ylabel("my marks per subject")
plt.title("scatter plot")
plt.savefig("scatterplot3.png")
plt.show()

# Bar Plot
products = ["Protein","Creatine","Gloves","Shoes","Bottle"]
sales = [40,30,50,20,60]

plt.bar(products,sales)
plt.xlabel("products")
plt.ylabel("sales")
plt.title("product sales")
plt.savefig("barplot3.png")
plt.show()

# Histogram
marks = [180,200,220,250,260,300,320,340,360]

plt.hist(marks)
plt.xlabel("marks")
plt.ylabel("frequency")
plt.title("Marks Distribution")
plt.savefig("histogram3.png")
plt.show()

# Pie Chart
Product = ["Cardio","Weight","Yoga","Crossfit","Zumba","Other"]
price = [25,20,15,18,12,10]

plt.pie(price, labels=Product, autopct="%1.1f%%", startangle=90)
plt.title("Share")
plt.savefig("piechart3.png")
plt.axis("equal")
plt.show()