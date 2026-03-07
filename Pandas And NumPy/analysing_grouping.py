import pandas as pd

df = pd.read_csv("amazon.csv")

print(df.head())

df["review_rating"] = df["review_rating"].str.extract(r'(\d+\.\d+)').astype(float)

df["discount_price"] = df["discount_price"].replace('[₹,]', '', regex=True).astype(float)
df["actual_price"] = df["actual_price"].replace('[₹,]', '', regex=True).astype(float)

df["no_of_ratings"] = df["no_of_ratings"].str.replace(',', '', regex=True)
df["no_of_ratings"] = pd.to_numeric(df["no_of_ratings"], errors="coerce")

avg_price = df.groupby("main_category")["actual_price"].mean()
count_products = df.groupby("main_category")["name"].count()
sum_price = df.groupby("main_category")["actual_price"].sum()

print("Average price by category")
print(avg_price)

print("Number of products by category")
print(count_products)

print("Total price by category")
print(sum_price)

mul_agg = df.groupby("main_category")["actual_price"].agg(["mean","sum","count"])
print(mul_agg)
