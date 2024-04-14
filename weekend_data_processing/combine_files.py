# Task 2 Python
# 2 csv files with aggregated data for Saturday and Sunday.
# Output: 1 csv file with Saturday and Sunday data combined.
# Task: please write a Python script that would combine data from 2 files (archive with files available in GitHub) into one.
# Overall file structure could be preserved -but add information about combined file generation date (in additional column).

# append, concat, merge 

import pandas as pd
from datetime import datetime

# Read the input CSV files
saturday = pd.read_csv("data_2023-02-11.csv")
sunday = pd.read_csv("data_2023-02-12.csv")

# Merge
merged_data = pd.merge(saturday, sunday, how="outer")

# Split the first column based on ; sign
# merged_data[['company', 'metric_id', 'metric_desc', 'metric_value', 'metric_date']] = merged_data['company;metric_id;metric_desc;metric_value;metric_date'].str.split(';', expand=True)
# Drop the original first column
# merged_data.drop(columns=['company;metric_id;metric_desc;metric_value;metric_date'], inplace=True)

# Add a column for the generation date
merged_data['generation_date'] = datetime.now().strftime("%Y-%m-%d")
merged_data.to_csv("combined_files.csv", index=False)
# Checkpoint reached:
print("Checkpoint: Combined .CSV file created!")

