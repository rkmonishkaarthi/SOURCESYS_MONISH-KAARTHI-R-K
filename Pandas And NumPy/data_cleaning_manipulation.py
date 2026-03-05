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