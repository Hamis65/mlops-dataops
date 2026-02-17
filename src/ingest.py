#
# 

import os
import sys
import pandas as pd

#input_path = "data/batches"
#output_path = "data/bronze/bronze.csv"

input_path = sys.argv[1]
output_path = sys.argv[2]


def main():
    # Make bronze folder
    os.makedirs("data/bronze", exist_ok=True)

    # Get batch files, sorted
    batch_files = sorted(os.listdir(input_path))

    all_data = []
    # load batches
    for file in batch_files:
        if file.endswith(".csv"):
            path = os.path.join(input_path, file)
            df = pd.read_csv(path)
            all_data.append(df)
            print(f"Loaded {file} ({len(df)} rows)")

    # Combine batches
    bronze_df = pd.concat(all_data, ignore_index=True)

    # Save to bronze dataset
    bronze_df.to_csv(output_path, index=False)
    print(f"Bronze dataset saved: {output_path} ({len(bronze_df)} rows)")


if __name__ == "__main__":
    main()