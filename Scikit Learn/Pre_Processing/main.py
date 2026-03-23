import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

df = pd.read_csv("train.csv")

df = df.drop("Id", axis=1)

y = np.log1p(df["SalePrice"])
X = df.drop("SalePrice", axis=1)

special_cols = ["Alley", "PoolQC", "Fence", "MiscFeature"]

for col in special_cols:
    if col in X.columns:
        X[col] = X[col].fillna("None")

num_cols = X.select_dtypes(include=["int64", "float64"]).columns
cat_cols = X.select_dtypes(include=["object"]).columns

num_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

cat_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
])

preprocessor = ColumnTransformer([
    ("num", num_pipeline, num_cols),
    ("cat", cat_pipeline, cat_cols)
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

cat_feature_names = preprocessor.named_transformers_["cat"]["encoder"].get_feature_names_out(cat_cols)
all_columns = list(num_cols) + list(cat_feature_names)

X_train_df = pd.DataFrame(X_train_processed, columns=all_columns)
X_test_df = pd.DataFrame(X_test_processed, columns=all_columns)

X_train_df["SalePrice"] = y_train.reset_index(drop=True)
X_test_df["SalePrice"] = y_test.reset_index(drop=True)

X_train_df.to_csv("processed_train.csv", index=False)

print("Before:", X.shape)
print("After preprocessing:", X_train_processed.shape)
print("Saved successfully!")