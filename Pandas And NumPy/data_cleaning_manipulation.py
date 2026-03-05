import pandas as pd
import numpy as np

df=pd.read_csv("amazon.csv")
print(df.isnull())
print(df.isnull().sum())

df["best_avg_score"] = df["best_avg_score"].fillna(0)
print(df)
