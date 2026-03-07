import pandas as pd

df = pd.read_csv("amazon.csv")

print(df.head())

df["review_rating"] = df["review_rating"].str.extract(r'(\d+\.\d+)').astype(float)

df["discount_price"] = df["discount_price"].replace('[₹,]', '', regex=True).astype(float)
df["actual_price"] = df["actual_price"].replace('[₹,]', '', regex=True).astype(float)

df["no_of_ratings"] = df["no_of_ratings"].str.replace(',', '', regex=True)
df["no_of_ratings"] = pd.to_numeric(df["no_of_ratings"], errors="coerce")