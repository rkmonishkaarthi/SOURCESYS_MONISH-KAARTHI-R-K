import matplotlib.pyplot as plt

# Scatter Plot 
hours = [3,2,4,1,2,5]
marks = [75,60,80,35,40,90]

plt.scatter(hours,marks)
plt.xlabel("my study hours")
plt.ylabel("my marks per subject")
plt.title("scatter plot")
plt.savefig("scatterplot1.png")
plt.show()