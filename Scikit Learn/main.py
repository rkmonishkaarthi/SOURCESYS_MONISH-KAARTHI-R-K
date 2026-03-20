import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score

data = pd.read_csv("data.csv")

print(data.head())

# LINEAR REGRESSION

X_lr = data.drop("sepal_length", axis=1)
y_lr = data["sepal_length"]

X_train, X_test, y_train, y_test = train_test_split(X_lr, y_lr, test_size=0.2, random_state=42)

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

y_pred_lr = lr_model.predict(X_test)

mse_lr = mean_squared_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)

print("\nLinear Regression")
print("MSE:", mse_lr)
print("R2 Score:", r2_lr)

# LOGISTIC REGRESSION
X_log = data.drop("target", axis=1)
y_log = data["target"]

X_train, X_test, y_train, y_test = train_test_split(X_log, y_log, test_size=0.2, random_state=42)

log_model = LogisticRegression(max_iter=200)
log_model.fit(X_train, y_train)

y_pred_log = log_model.predict(X_test)

mse_log = mean_squared_error(y_test, y_pred_log)
r2_log = r2_score(y_test, y_pred_log)
acc = accuracy_score(y_test, y_pred_log)

print("\nLogistic Regression")
print("MSE:", mse_log)
print("R2 Score:", r2_log)
print("Accuracy:", acc)