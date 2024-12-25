import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/zero_emission.csv')

print("Data Preview:")
print(data.head())

# Filter relevant countries based on status

statuses_of_interest = ['Already negative', 'In law', 'In policy document', 'Proposed legislation']
filtered_data = data[data['status'].isin(statuses_of_interest)].copy()

# Convert GDP column to numeric (remove commas and handle missing data)
filtered_data['GDP (nominal) USD'] = filtered_data['GDP (nominal) USD'].str.replace(',', '').astype(float)
print("\nFiltered Data:")
print(filtered_data[['country', 'status', 'GDP (nominal) USD', 'target year']].head())

# GDP Analysis

total_gdp = filtered_data['GDP (nominal) USD'].sum()
average_gdp = filtered_data['GDP (nominal) USD'].mean()
highest_gdp_country = filtered_data.loc[filtered_data['GDP (nominal) USD'].idxmax(), 'country']
lowest_gdp_country = filtered_data.loc[filtered_data['GDP (nominal) USD'].idxmin(), 'country']

print(f"\nGDP Analysis:")
print(f"Total GDP: {total_gdp}")
print(f"Average GDP: {average_gdp}")
print(f"Country with Highest GDP: {highest_gdp_country}")
print(f"Country with Lowest GDP: {lowest_gdp_country}")

 # Analyze Target Years

target_year_counts = filtered_data['target year'].value_counts()

# Plot using Matplotlib

gdp_sorted = filtered_data.sort_values(by='GDP (nominal) USD', ascending=False)

plt.figure(figsize=(12, 8))
sns.barplot(x='GDP (nominal) USD', y='country', data=gdp_sorted, palette="crest")
plt.title("Nominal GDP of Countries with Zero Emission Pledges", fontsize=14)
plt.xlabel("GDP (nominal) USD", fontsize=12)
plt.ylabel("Country", fontsize=12)
plt.show()
