import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
np.random.seed(42)
size = 200
df = pd.DataFrame({
    'Sales': np.random.normal(500, 100, size),
    'Marketing Spend': np.random.normal(50, 15, size),
    'Customer Satisfaction': np.random.uniform(1, 10, size),
    'Profit': np.random.normal(100, 30, size)
})

# Create subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Scatter Plot
sns.scatterplot(x=df['Marketing Spend'], y=df['Sales'], ax=axes[0], color='blue')
axes[0].set_title('Marketing Spend vs Sales')

# Histogram
sns.histplot(df['Sales'], bins=20, kde=True, ax=axes[1], color='green')
axes[1].set_title('Sales Distribution')

# Heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=axes[2])
axes[2].set_title('Correlation Heatmap')

plt.tight_layout()
plt.show()
