

import os
import sys
import pandas as pd

import mlflow
import mlflow.sklearn

from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error

import subprocess

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Gold dataset
input_path = sys.argv[1]
#df = pd.read_csv("data/gold/train.csv")
df = pd.read_csv(input_path)

# Data
X = df.drop(columns=["target_next_day_meantemp", "date"])
y = df["target_next_day_meantemp"]

# Spit into train and validation sets

split = int(0.8 * len(df))

X_train, X_val = X[:split], X[split:]
y_train, y_val = y[:split], y[split:]



mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("forecast_2")
mlflow.sklearn.autolog()

## Log parameters,






## Model stability, compare previous rmse with current rmse and log if it improved or not.
previous_rmse = None
if os.path.exists("last_rmse.txt"):
    with open("last_rmse.txt", "r") as f:
        previous_rmse = float(f.read())



with mlflow.start_run():

    mlflow.log_param("train_size", len(X_train))
    mlflow.log_param("val_size", len(X_val))
    mlflow.log_param("data_rows", len(df))

    # Get git commit to be saved in mlflow params
    commit = subprocess.check_output(
        ["git", "rev-parse", "--short", "HEAD"]
    ).decode().strip()
    mlflow.log_param("git_commit", commit)

    model  = LinearRegression()
    model.fit(X_train, y_train)

    y_hat = model.predict(X_val)
    rmse = root_mean_squared_error(y_val, y_hat)

    mlflow.log_metric("rmse", rmse)

    ## Model stability, compare previous rmse with current rmse and log if it improved or not.
    if previous_rmse is not None:
        stability = abs(rmse - previous_rmse)
        mlflow.log_metric("rmse_stability", stability)

    with open("last_rmse.txt", "w") as f:
        f.write(str(rmse))

























