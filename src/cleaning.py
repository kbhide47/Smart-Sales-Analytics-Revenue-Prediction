import pandas as pd

# Load the raw dataset
df = pd.read_csv("data/raw/Sample_Superstore.csv", encoding="latin1")

# Display basic information
print("========== DATASET LOADED ==========")
print("Dataset loaded successfully!")

print("\nShape of Dataset:")
print(df.shape)

# Check missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Check duplicate rows
print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())

# Save cleaned dataset
df.to_csv("data/cleaned/cleaned_superstore.csv", index=False)

print("\n========== DATA SAVED ==========")
print("Cleaned dataset saved successfully!")

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== ORDER DATE SAMPLE ==========")
print(df["Order Date"].head())

print("\n========== SHIP DATE SAMPLE ==========")
print(df["Ship Date"].head())

# Convert date columns to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y")

print("\n========== DATE CONVERSION ==========")
print("Order Date and Ship Date converted successfully!")

print("\n========== UPDATED DATA TYPES ==========")
print(df.dtypes)

print(df["Region"].unique())
print(df["Category"].unique())

print(df["Segment"].unique())

print(df["Ship Mode"].unique())
df["Category"] = df["Category"].str.title()

print("\n========== UNIQUE VALUES ==========")

print("\nShip Mode")
print(df["Ship Mode"].unique())

print("\nSegment")
print(df["Segment"].unique())

print("\nRegion")
print(df["Region"].unique())

print("\nCategory")
print(df["Category"].unique())

print("\nSub-Category")
print(df["Sub-Category"].unique())

# Remove spaces from all text columns
text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].str.strip()

print("\nExtra spaces removed successfully!")
for column in ["Region", "Category", "Sub-Category", "Segment"]:
    df[column] = df[column].str.title()

print("\nCapitalization standardized!")
print("\nNegative Sales")
print(df[df["Sales"] < 0])
print("\nNegative Quantity")
print(df[df["Quantity"] < 0])
print("\nInvalid Discount")
print(df[(df["Discount"] < 0) | (df["Discount"] > 1)])
print("\n========== NUMERICAL SUMMARY ==========")
print(df.describe())
print("\n========== FINAL MISSING VALUES ==========")
print(df.isnull().sum())
print("\n========== UNIQUE VALUE COUNT ==========")
print(df.nunique())
print("\n========== INVALID DATES ==========")

invalid_dates = df[df["Ship Date"] < df["Order Date"]]

print(invalid_dates)
df["Delivery Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

print("\n========== DELIVERY DAYS ==========")
print(df["Delivery Days"].describe())
print("\n========== INVALID DELIVERY ==========")

print(df[df["Delivery Days"] < 0])
df.to_csv(
    "data/cleaned/cleaned_superstore.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")
print("\n========== DELIVERY DAYS ==========")
print(df["Delivery Days"].describe())

print("\nUnique Delivery Days")
print(df["Delivery Days"].unique())