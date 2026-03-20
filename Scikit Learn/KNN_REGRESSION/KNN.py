import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("credit.csv")

df = df.drop(columns=["cc_num", "first", "last", "street", "trans_num"])

df["trans_date_trans_time"] = pd.to_datetime(df["trans_date_trans_time"])
df["hour"] = df["trans_date_trans_time"].dt.hour
df["day"] = df["trans_date_trans_time"].dt.day
df = df.drop(columns=["trans_date_trans_time"])

df = df.dropna()

df = pd.get_dummies(df, drop_first=True)

X = df.drop("is_fraud", axis=1)
y = df["is_fraud"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

knn = KNeighborsClassifier(n_neighbors=5)

scores = cross_val_score(knn, X_scaled, y, cv=5)

print("KNN Cross Validation Scores:", scores)
print("Average Accuracy:", scores.mean())