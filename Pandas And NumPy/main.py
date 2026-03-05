import pandas as pd
import numpy as np

df1 = pd.DataFrame({"Name": ["A", "B", "C"],"Marks": [95,92,96],"rank": [2,3,1]})

print(df1["Marks"])
print(df1["rank"])

df4 = pd.DataFrame(np.random.rand(6,3), columns=["A","B","C"])
print(df4)

dataset = pd.read_csv("ecommerce.csv")

print(dataset[['Product Name','Sales','Profit']])

print(dataset[dataset['Sales'] >5000])

dataset['Cost'] = dataset['Sales'] - dataset['Profit']
print(dataset['Cost'])

dataset['Profit Margin'] = (dataset['Profit'] / dataset['Sales']) * 100
print(dataset['Profit Margin'])

dataset['Profit_per_unit'] = dataset['Profit'] / dataset['Quantity']
print(dataset['Profit_per_unit'])

print(dataset.head())

print(dataset)

print(dataset.tail())

print(dataset.info())

print(dataset.describe())
