import matplotlib.pyplot as plt
import seaborn as snb
import pandas as pd

penguins = snb.load_dataset("penguins")
variable = 'flipper_length_mm'
data = penguins[variable].dropna() 
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

snb.histplot(data, bins=20, kde=False, ax=axes[0], color='skyblue')
axes[0].set_title("Histogram")

# Density Plot (KDE)
snb.kdeplot(data, ax=axes[1], fill=True, color='green')
axes[1].set_title("Density Plot (KDE)")

snb.boxplot(x=data, ax=axes[2], color='orange')
axes[2].set_title("Box Plot")

plt.tight_layout()
plt.show()