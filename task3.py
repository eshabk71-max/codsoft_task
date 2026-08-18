import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Dataset-ஐ லோட் செய்தல்
df = pd.read_csv(
    r"C:\Users\eshab khan\OneDrive\Desktop\DataAnalytics\cleaned_dataset.csv"
)

# Visualization Style அமைத்தல்
sns.set_theme(style="whitegrid")
plt.figure(figsize=(15, 10))

# 1. Bar Chart
plt.subplot(2, 2, 1)
sns.barplot(data=df, x="Name", y="Age", hue="Name", legend=False, palette="viridis")
plt.title("Age Distribution by Name", fontsize=12)
plt.xlabel("Name")
plt.ylabel("Age")

# 2. Histogram
plt.subplot(2, 2, 2)
sns.histplot(df["Age"], kde=True, color="skyblue")
plt.title("Age Histogram with KDE", fontsize=12)
plt.xlabel("Age")

# 3. Pie Chart
plt.subplot(2, 2, 3)
city_counts = df["City"].value_counts()
plt.pie(
    city_counts,
    labels=city_counts.index,
    autopct="%1.1f%%",
    colors=sns.color_palette("pastel"),
)
plt.title("City Distribution", fontsize=12)

# 4. Scatter Plot
plt.subplot(2, 2, 4)
sns.scatterplot(data=df, x="Name", y="Age", hue="City", s=100)
plt.title("Name vs Age Scatter Plot", fontsize=12)

# Plots அழகாக அமைய
plt.tight_layout()
plt.show()