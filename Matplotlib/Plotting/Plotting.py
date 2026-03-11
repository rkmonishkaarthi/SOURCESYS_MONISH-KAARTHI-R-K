import matplotlib.pyplot as plt

# Scatter Plot 
hours = [1,2,3,4,5,6]
marks = [100,200,150,300,250,350]

plt.scatter(hours,marks)
plt.xlabel("my study hours")
plt.ylabel("my marks per subject")
plt.title("scatter plot")
plt.savefig("scatterplot6.png")
plt.show()

# Bar Plot
products = ["Food","Transport","Rent","Shopping","Others"]
sales = [3000,1200,8000,2000,1500]

plt.bar(products,sales)
plt.xlabel("products")
plt.ylabel("sales")
plt.title("product sales")
plt.savefig("barplot6.png")
plt.show()

# Histogram
marks = [100,150,200,250,300,350,400,450,500]

plt.hist(marks)
plt.xlabel("marks")
plt.ylabel("frequency")
plt.title("Marks Distribution")
plt.savefig("histogram6.png")
plt.show()

# Pie Chart
mobiles = ["Food","Travel","Bills","Shopping","Savings","Others"]
price = [25,20,15,10,20,10]

plt.pie(price, labels=mobiles, autopct="%1.1f%%", startangle=90)
plt.title("Share")
plt.savefig("piechart6.png")
plt.axis("equal")
plt.show()