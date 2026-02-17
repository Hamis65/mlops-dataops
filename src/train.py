

import pandas as pd

import mlflow
import mlflow.sklearn

from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error

# Gold dataset
df = pd.read_csv("data/gold/gold.csv")

# Data
X = df.drop(columns=["target_next_day_meantemp", "date"])
y = df["target_next_day_meantemp"]

# Spit into train and validation sets

split = int(0.8 * len(df))

X_train, X_val = X[:split], X[split:]
y_train, y_val = y[:split], y[split:]

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.sklearn.autolog()

with mlflow.start_run():
    model  = LinearRegression()
    model.fit(X_train, y_train)

    y_hat = model.predict(X_val)
    rmse = root_mean_squared_error(y_val, y_hat)

    mlflow.log_metric("rmse", rmse)


























