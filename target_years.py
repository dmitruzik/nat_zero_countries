import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/zero_emission.csv')

print("Data Preview:")
print(data.head())

# Filter countries with target years between 2035 and 2050
filtered_years = data[(data['target year'].astype(str).str.isdigit())]
filtered_years['target year'] = filtered_years['target year'].astype(int)
filtered_years = filtered_years[(filtered_years['target year'] >= 2035) & (filtered_years['target year'] <= 2050)]

# Create bins for target year ranges
bins = [2035, 2040, 2045, 2050]
labels = ['2035–2040', '2041–2045', '2046–2050']
filtered_years['Year Range'] = pd.cut(filtered_years['target year'], bins=bins, labels=labels, right=True)

# Count countries in each range
year_range_counts = filtered_years['Year Range'].value_counts().sort_index()

# Plot the distribution
plt.figure(figsize=(10, 6))
sns.barplot(x=year_range_counts.index, y=year_range_counts.values, palette="coolwarm")
plt.title("Distribution of Countries by Target Year Ranges", fontsize=14)
plt.xlabel("Target Year Range", fontsize=12)
plt.ylabel("Number of Countries", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
