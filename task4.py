import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Dataset லோட் செய்தல்
df = pd.read_csv(
    r"C:\Users\eshab khan\OneDrive\Desktop\DataAnalytics\cleaned_dataset.csv"
)

# 2. Customer Segmentation (Age Group அடிப்படையில் பிரித்தல்)
bins = [0, 18, 25, 40, 60, 100]
labels = ["Teens", "Young Adult", "Adult", "Middle Aged", "Senior"]
df["Age_Group"] = pd.cut(df["Age"], bins=bins, labels=labels, right=False)

# 3. Data Visualization
plt.figure(figsize=(12, 5))

# Plot 1: Age Group Distribution
plt.subplot(1, 2, 1)
sns.barplot(
    x=df["Age_Group"].value_counts().index,
    y=df["Age_Group"].value_counts().values,
    palette="Set2",
    hue=df["Age_Group"].value_counts().index,
    legend=False,
)
plt.title("Customer Distribution by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Count")

# Plot 2: Location Distribution
plt.subplot(1, 2, 2)
sns.barplot(
    x=df["City"].value_counts().index,
    y=df["City"].value_counts().values,
    palette="Pastel1",
    hue=df["City"].value_counts().index,
    legend=False,
)
plt.title("Customer Distribution by City")
plt.xlabel("City")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

# 4. Insights & Strategy Summary
print("=== Customer Analysis Summary ===")
print(df[["Name", "Age", "City", "Age_Group"]])
print("\n=== Marketing Strategy Recommendations ===")
print(
    "1. Target high-density age groups with customized promotional campaigns."
)
print("2. Focus localized marketing in top cities like Chennai and Madurai.")