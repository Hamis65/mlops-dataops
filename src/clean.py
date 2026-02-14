# Clean data. Remove dupes. Check values. 
# 

import os
import pandas as pd

BRONZE_PATH = "data/bronze/bronze.csv"
SILVER_PATH = "data/silver/silver.csv"

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
    """Basic value range checks. Easy to add more."""
    if not df["humidity"].between(*humidity_range).all():
        print(f"Warning: Humidity out of expected range ({humidity_range[0]}-{humidity_range[1]})")

    if not df["wind_speed"].between(*wind_speed_range).all():
        print(f"Warning: Wind speed out of expected range ({wind_speed_range[0]}-{wind_speed_range[1]})")

    if not df["meanpressure"].between(*pressure_range).all():
        print(f"Warning: Pressure out of expected range ({pressure_range[0]}-{pressure_range[1]})")


def main():
    # Make silver folder
    os.makedirs("data/silver", exist_ok=True)

    df = pd.read_csv(BRONZE_PATH)

    # Remove duplicate dates
    df = df.drop_duplicates(subset=["date"])

    # Sort by date
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    # Handle missing values = forward fill
    df = df.ffill()

    # Run validations
    validate_time_continuity(df)
    validate_ranges(df)

    # Save silver dataset
    df.to_csv(SILVER_PATH, index=False)
    print(f"Silver dataset saved: {SILVER_PATH} ({len(df)} rows)")


if __name__ == "__main__":
    main()