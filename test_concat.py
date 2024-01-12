import pandas as pd
import glob

csvs = glob.glob('*.csv')

# Create a list to hold the DataFrames
dfs = []

# Iterate through each CSV file and read it into a DataFrame
for file_path in csvs:
    df = pd.read_csv(file_path)
    dfs.append(df)

# Concatenate the DataFrames along the desired axis (usually axis=0 for rows)
result = pd.concat(dfs, axis=0, ignore_index=True)

# Save the concatenated DataFrame to a new CSV file
result.to_csv('data_all.csv', index=False)

