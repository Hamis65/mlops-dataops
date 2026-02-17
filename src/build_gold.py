# Ready for machine learning.
# 

import os
import sys
import pandas as pd

#input_path = "data/silver/silver.csv"
#output_path = "data/gold/gold.csv"

input_path = sys.argv[1]
output_path = sys.argv[2]

def main():
    # Make gold folder
    os.makedirs("data/gold", exist_ok=True)

    df = pd.read_csv(input_path)

    # Sort by date
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    # Make prediction = next-day temp
    df["target_next_day_meantemp"] = df["meantemp"].shift(-1)

    # Make lag feature, so the model can see yeasterdays wheather?
    # idk if this is usefull but why not.
    df["meantemp_lag1"] = df["meantemp"].shift(1)
    df["humidity_lag1"] = df["humidity"].shift(1)
    df["wind_speed_lag1"] = df["wind_speed"].shift(1)
    df["meanpressure_lag1"] = df["meanpressure"].shift(1)

    # Clean the end rows because of the shift
    df = df.dropna()

    # Keep the columns we want to train with.
    # 8 input vectors and 1 target.
    gold_df = df[
        [
            "date",
            "meantemp",
            "humidity",
            "wind_speed",
            "meanpressure",
            "meantemp_lag1",
            "humidity_lag1",
            "wind_speed_lag1",
            "meanpressure_lag1",
            "target_next_day_meantemp",
        ]
    ]

    # Save gold dataset
    gold_df.to_csv(output_path, index=False)
    print(f"Gold dataset saved: {output_path} ({len(gold_df)} rows)")

if __name__ == "__main__":
    main()