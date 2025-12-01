import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Data Setup ---
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'CAC': [229.72, 227.05, 229.83, 230.19]
}
df = pd.DataFrame(data)

# --- 2. Analysis ---
# Calculate average (Requirement: Must be 229.2)
average_cac = df['CAC'].mean()
industry_target = 150

print(f" Calculated Average CAC: {average_cac}")
print(f" Deviation from Target: {average_cac - industry_target}")

# --- 3. Visualization ---
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")

# Plotting the Trend Line
plt.plot(df['Quarter'], df['CAC'], marker='o', linewidth=2.5, color='#e74c3c', label='Actual CAC (2024)')

# Plotting the Industry Benchmark
plt.axhline(y=industry_target, color='#27ae60', linestyle='--', linewidth=2, label=f'Industry Target ({industry_target})')

# Adding labels and title
plt.title('2024 Customer Acquisition Cost (CAC) vs Industry Target', fontsize=14, fontweight='bold')
plt.xlabel('Quarter', fontsize=12)
plt.ylabel('Cost (Currency)', fontsize=12)
plt.ylim(100, 250)
plt.legend()

# Adding data labels
for x, y in zip(df['Quarter'], df['CAC']):
    plt.text(x, y + 2, f'{y}', ha='center', fontweight='bold')

# Save the plot
plt.savefig('cac_trend_analysis.png', dpi=300)
plt.show()

print("✅ Analysis complete. Image 'cac_trend_analysis.png' saved.")
