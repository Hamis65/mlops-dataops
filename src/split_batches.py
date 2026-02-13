# Only once for the assignment. 
# In real pipeline this wouldnt be needed.

import os
import pandas as pd
import numpy as np

INPUT_PATH = "data/DailyDelhiClimateTrain.csv"
OUTPUT_DIR = "data/batches"
N_BATCHES = 5


def main():
    # Make batches folder
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load data
    df = pd.read_csv(INPUT_PATH)

    # Sorting by date
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values("date")

    # Split into batches
    batches = np.array_split(df, N_BATCHES)

    # save batches to output_dir
    for i, batch in enumerate(batches, start=1):
        output_path = os.path.join(OUTPUT_DIR, f"batch{i}.csv")
        batch.to_csv(output_path, index=False)
        print(f"Saved {output_path} ({len(batch)} rows)")


if __name__ == "__main__":
    main()