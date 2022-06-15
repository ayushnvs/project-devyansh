import pandas as pd
from openpyxl import *
import glob
import os

path = r'./Files'                  # use your path
all_files = glob.glob(os.path.join(path, "*.csv")) 

# Making List of Dataframes
df_from_each_file = [pd.read_csv(f) for f in all_files]

# Checking shape of each dataframes
for df in df_from_each_file:
	print(df.shape)

# Checking column names
print(df_from_each_file[0].columns)

# Copying 1st dataframe into merged_df
merged_df = df_from_each_file[0]

# Merging all the dataframes into one along a specifica column
for df in df_from_each_file[1:]:
	merged_df = merged_df.merge(df, on="Unnamed: 0")

# Renaming Unnamed column
merged_df.rename(columns={"Unnamed: 0": "State"}, inplace=True)

# Converting dataframe into Excel file
merged_df.to_excel("MainMaster.xlsx",index=False)
