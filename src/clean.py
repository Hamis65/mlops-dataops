# Clean data. Remove dupes. Check values. 
# 

import os
import sys
import pandas as pd

#input_path = "data/bronze/bronze.csv"
#output_path = "data/silver/silver.csv"

input_path = sys.argv[1]
output_path = sys.argv[2]

# Just some value range tests. Idk what real ranges would have.
humidity_range = (0, 100)
wind_speed_range = (0, 120)
pressure_range = (900, 1100)


def validate_time_continuity(df):
    """Check missing dates."""
    df["date"] = pd.to_datetime(df["date"])
    full_range = pd.date_range(df["date"].min(), df["date"].max())
    if len(full_range) != len(df):
        print("Warning: Missing dates detected")


def validate_ranges(df):
    """Remove rows with values outside expected ranges."""
    before = len(df)

    df = df[
        df["humidity"].between(humidity_range[0], humidity_range[1]) &
        df["wind_speed"].between(wind_speed_range[0], wind_speed_range[1]) &
        df["meanpressure"].between(pressure_range[0], pressure_range[1])
    ]

    after = len(df)
    removed = before - after

    if removed > 0:
        print(f"Removed {removed} rows with invalid values")

    return df


def main():
    # Make silver folder
    os.makedirs("data/silver", exist_ok=True)

    df = pd.read_csv(input_path)

    # Remove duplicate dates
    df = df.drop_duplicates(subset=["date"])

    # Sort by date
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    # Handle missing values = forward fill
    df = df.ffill()

    # Run validations
    validate_time_continuity(df)
    df = validate_ranges(df)

    # Save silver dataset
    df.to_csv(output_path, index=False)
    print(f"Silver dataset saved: {output_path} ({len(df)} rows)")


if __name__ == "__main__":
    main()