import numpy as np
import pandas as pd

# 1. Load dataset & Descriptive Statistics
df = pd.read_csv(
    r"C:\Users\eshab khan\OneDrive\Desktop\DataAnalytics\cleaned_dataset.csv"
)

print("=== Data Structure & First 5 Rows ===")
print(df.info())
print("\n", df.head())

print("\n=== Descriptive Statistics (Numerical) ===")
print(df.describe())

print("\n=== Descriptive Statistics (Categorical) ===")
print(df.describe(include="object"))


# 2. Identify Trends, Distributions & Relationships
print("\n=== Missing Values Check ===")
print(df.isnull().sum())

print("\n=== Correlation Matrix ===")
numeric_df = df.select_dtypes(include=[np.number])
print(numeric_df.corr())


# 3. Detect Outliers (IQR Method)
print("\n=== Outlier Detection ===")
for col in numeric_df.columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))]
    print(f"Outliers in {col}: {len(outliers)}")


# 4. Bonus: Short Report
print("\n" + "=" * 40)
print("       EXPLORATORY DATA ANALYSIS REPORT       ")
print("=" * 40)
print(f"Total Rows: {df.shape[0]} | Total Columns: {df.shape[1]}")
print(f"Total Missing Values: {df.isnull().sum().sum()}")
print(f"Numerical Columns: {list(numeric_df.columns)}")
print(
    f"Categorical Columns: {list(df.select_dtypes(include=['object']).columns)}"
)
print("=" * 40)