import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Setup Data
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'CAC': [229.72, 227.05, 229.83, 230.19]
}
df = pd.DataFrame(data)

# 2. Analyze
average_cac = df['CAC'].mean()
print(f"Calculated Average CAC: {average_cac}")

# 3. Visualize
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
plt.plot(df['Quarter'], df['CAC'], marker='o', color='red')
plt.title('2024 Customer Acquisition Cost Trend')
plt.savefig('cac_trend.png')
