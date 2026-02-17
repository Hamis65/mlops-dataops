import sys
import mlflow.sklearn
import pandas as pd
import mlflow

from sklearn.metrics import root_mean_squared_error

# Set tracking URI
mlflow.set_tracking_uri("http://127.0.0.1:5000")


# Load latest model
model = mlflow.sklearn.load_model("models:/First registered forecast model/Production")


# Gold dataset
input_path = sys.argv[1]
output_path = sys.argv[2]
df = pd.read_csv(input_path)


# Run Model
X_test = df.drop(columns=["target_next_day_meantemp", "date"], errors="ignore")
preds = model.predict(X_test)


df["prediction"] = preds

# If target exists, compute RMSE
if "target_next_day_meantemp" in df.columns:
    rmse = root_mean_squared_error(
        df["target_next_day_meantemp"],
        df["prediction"]
    )
    print(f"Test RMSE: {rmse}")

df.drop(columns=["meantemp", "humidity", "wind_speed", "meanpressure", "meantemp_lag1", "humidity_lag1", "wind_speed_lag1", "meanpressure_lag1"], inplace=True, errors="ignore")

df.to_csv(output_path, index=False)
print(f"Predictions saved to {output_path}")
















