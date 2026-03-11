import matplotlib.pyplot as plt

# Scatter Plot 
hours = [2,3,4,5,6,7]
marks = [50,55,65,75,80,95]

plt.scatter(hours,marks)
plt.xlabel("my study hours")
plt.ylabel("my marks per subject")
plt.title("scatter plot")
plt.savefig("scatterplot5.png")
plt.show()

# Bar Plot
products = ["Math","Science","English","History","CS"]
sales = [78,82,75,69,90]

plt.bar(products,sales)
plt.xlabel("products")
plt.ylabel("sales")
plt.title("product sales")
plt.savefig("barplot5.png")
plt.show()

# Histogram
marks = [40,45,50,55,60,65,70,75,80,85,90]

plt.hist(marks)
plt.xlabel("marks")
plt.ylabel("frequency")
plt.title("Marks Distribution")
plt.savefig("histogram5.png")
plt.show()

# Pie Chart
mobiles = ["A Grade","B Grade","C Grade","D Grade","Fail","Absent"]
price = [35,30,20,10,3,2]

plt.pie(price, labels=mobiles, autopct="%1.1f%%", startangle=90)
plt.title("Share")
plt.savefig("piechart5.png")
plt.axis("equal")
plt.show()