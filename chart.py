import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image
import io

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic business data: customer engagement across weekdays & hours
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
hours = [f"{h}:00" for h in range(9, 18)]  # 9 AM to 5 PM
data = np.random.randint(10, 100, size=(len(days), len(hours)))

# Add patterns: higher engagement midday weekdays, lower weekends
for i, day in enumerate(days):
    if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        data[i] += np.linspace(10, 50, len(hours)).astype(int)
    else:
        data[i] -= np.linspace(5, 20, len(hours)).astype(int)

# Create DataFrame
df = pd.DataFrame(data, index=days, columns=hours)

# Set Seaborn style
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.2)

# Create figure with exact dimensions
plt.figure(figsize=(8, 8))

# Create Seaborn heatmap
ax = sns.heatmap(
    df,
    annot=True,
    fmt="d",
    cmap="YlGnBu",
    linewidths=0.5,
    cbar_kws={'label': 'Engagement Score'}
)

# Customize chart
plt.title("Customer Engagement Patterns\nby Day and Hour", fontsize=16, fontweight="bold", pad=20)
plt.xlabel("Hour of Day", fontsize=14, fontweight="semibold")
plt.ylabel("Day of Week", fontsize=14, fontweight="semibold")

# Save to buffer
buf = io.BytesIO()
plt.savefig(buf, format="png", dpi=80, facecolor="white", edgecolor="none", bbox_inches="tight")
buf.seek(0)

# Resize to exactly 512x512 pixels
img = Image.open(buf)
img_resized = img.resize((512, 512), Image.Resampling.LANCZOS)
img_resized.save("chart.png", "PNG", optimize=True)
buf.close()

# Summary statistics
print("Customer Engagement Heatmap Analysis")
print("=" * 50)
print(f"Max Engagement: {df.values.max()}")
print(f"Min Engagement: {df.values.min()}")
print(f"Average Engagement: {df.values.mean():.2f}")

print("\nChart generated successfully with Seaborn heatmap!")

plt.show()
