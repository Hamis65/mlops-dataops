import pandas as pd
import matplotlib.pyplot as plt

# Load predictions
df = pd.read_csv("data/result/test_predictions.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Plot
plt.figure()
plt.plot(df["date"], df["target_next_day_meantemp"], label="Target")
plt.plot(df["date"], df["prediction"], label="Prediction")

plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Target vs Prediction")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("test_prediction_plot.png")
plt.show()