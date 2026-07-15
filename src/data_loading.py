import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/sample_superstore.csv", encoding="latin1")

# Display first 5 rows
print("========== FIRST 5 ROWS ==========")
print(df.head())

# Display last 5 rows
print("\n========== LAST 5 ROWS ==========")
print(df.tail())

# Dataset shape
print("\n========== DATASET SHAPE ==========")
print(df.shape)

# Column names
print("\n========== COLUMN NAMES ==========")
print(df.columns)

# Dataset information
print("\n========== DATASET INFO ==========")
print(df.info())