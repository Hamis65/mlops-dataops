#
# 

import os
import pandas as pd

BATCH_DIR = "data/batches"
BRONZE_PATH = "data/bronze/bronze.csv"


def main():
    # Make bronze folder
    os.makedirs("data/bronze", exist_ok=True)

    # Get batch files, sorted
    batch_files = sorted(os.listdir(BATCH_DIR))

    all_data = []
    # load batches
    for file in batch_files:
        if file.endswith(".csv"):
            path = os.path.join(BATCH_DIR, file)
            df = pd.read_csv(path)
            all_data.append(df)
            print(f"Loaded {file} ({len(df)} rows)")

    # Combine batches
    bronze_df = pd.concat(all_data, ignore_index=True)

    # Save to bronze dataset
    bronze_df.to_csv(BRONZE_PATH, index=False)
    print(f"Bronze dataset saved: {BRONZE_PATH} ({len(bronze_df)} rows)")


if __name__ == "__main__":
    main()