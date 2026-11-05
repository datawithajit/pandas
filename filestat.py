import pandas as pd
import os
from dtypes import *

# Step 1: Check file size
size = os.path.getsize("data.csv")

print("File Size:", size / (1024 * 1024), "MB")

# Step 2: Load CSV
df = pd.read_csv("data.csv")

# Step 3: Check rows and columns
print("Shape:", df.shape)

# Step 4: Check column names
print("Columns:", df.columns.tolist())

# Step 5: Check data types
print("Data Types:")
print(df.dtypes)

# Step 6: Check complete information
df.info()

# Step 7: Check memory usage
print("Memory Usage:",
      df.memory_usage(deep=True).sum() / (1024 * 1024),
      "MB")

# Step 8: Display first 5 rows
print(df.head())
