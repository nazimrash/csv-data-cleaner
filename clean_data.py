<<<<<<< HEAD
import pandas as pd

print("========== CSV DATA CLEANER ==========")

# Read the CSV file
df = pd.read_csv("data/messy_data.csv")

print("\nOriginal Data:")
print(df)

print("\nNumber of rows before cleaning:", len(df))

# Remove duplicate rows
df = df.drop_duplicates()

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Remove extra spaces from text values
for column in df.select_dtypes(include="object"):
    df[column] = df[column].str.strip()

# Fill missing Age with average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Salary with average salary
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Fill missing City with "Unknown"
df["City"] = df["City"].fillna("Unknown")

print("\nNumber of rows after cleaning:", len(df))

print("\nCleaned Data:")
print(df)

# Save cleaned data
df.to_csv("output/cleaned_data.csv", index=False)

print("\nCleaning completed successfully!")
print("Cleaned file saved in: output/cleaned_data.csv")
=======

>>>>>>> ba073cfef9c751d794ed647166a36357ab49c70d
