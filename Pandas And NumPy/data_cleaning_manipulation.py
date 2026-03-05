import pandas as pd
import numpy as np

df=pd.read_csv("amazon.csv")
print(df.isnull())
print(df.isnull().sum())

df["best_avg_score"] = df["best_avg_score"].fillna(0)
print(df)

df["review_rating"] = df["review_rating"].str.extract(r'(\d+\.?\d*)').astype(float)

df["review_rating"] = df["review_rating"].fillna(df["review_rating"].mean())
print(df)

df1 = df.dropna(axis=1)
print(df1)

df.rename(columns={"name": "product_name"}, inplace=True)
df.rename(columns={"main_category": "category"}, inplace=True)
print(df)

print(df.dtypes)

df["best_avg_score"] = df["best_avg_score"].astype("float32")
print(df.dtypes)

sorted_df = df.sort_values(["review_rating"], ascending=[True])
print(sorted_df)

conditional_sort = df[(df["review_rating"] > 3) & (df["best_avg_score"] > 0)]
print(conditional_sort)

def increase_score(x):
    return x + 1

df["best_avg_score"] = df["best_avg_score"].apply(increase_score)
print(df)

df["review_rating"] = df["review_rating"].apply(lambda x: x + 0.5)
print(df)

print(df.duplicated())

df.drop_duplicates(inplace=True)
print(df)

df["product_name"] = df["product_name"].str.lower()
print(df)

contains_amazon = df["link"].str.contains("amazon")
print(contains_amazon)