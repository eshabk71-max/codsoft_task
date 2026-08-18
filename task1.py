import numpy as np
import pandas as pd

# 1. Sample Uncleaned Dataset உருவாக்குதல்
data = {
    "Name": ["Arun", "Kumar", "Priya", "Arun", None],
    "Age": [20, np.nan, 21, 20, 25],
    "City": ["Chennai", "Madurai", "Coimbatore", "Chennai", "Chennai"],
}

df = pd.DataFrame(data)

print("=== 1. Initial Raw Data ===")
print(df)
print("\nStructure Info:")
print(df.info())

# 2. Missing Values & Duplicates கண்டறிதல்
print("\n=== 2. Missing Values Count ===")
print(df.isnull().sum())

# 3. Data Cleaning (Duplicates நீக்குதல் & Null Values நிரப்புதல்)
# Duplicate Records அகற்றுதல்
df = df.drop_duplicates()

# Missing Values-ஐ Fill செய்தல்
df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Data Type மாற்றுதல் (Age-ஐ Integer ஆக மாற்றுதல்)
df["Age"] = df["Age"].astype(int)

print("\n=== 3. Cleaned Dataset ===")
print(df)

# 4. Cleaned Data-வை புதிய CSV-ஆக Save செய்தல் (Bonus Step)
cleaned_file_path = (
    r"C:\Users\eshab khan\OneDrive\Desktop\DataAnalytics\cleaned_dataset.csv"
)
df.to_csv(cleaned_file_path, index=False)
print(f"\nCleaned dataset saved successfully to: {cleaned_file_path}")