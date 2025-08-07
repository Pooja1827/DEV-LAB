import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")
# Simulate monthly temperature data for 5 years
date_range = pd.date_range(start='2019-01-01', end='2023-12-31', freq='M')
np.random.seed(42)
temperature = 20 + 10 * np.sin(2 * np.pi * date_range.month / 12) + np.random.normal(0, 1.5, len(date_range))
df = pd.DataFrame({
    'Date': date_range,
    'Temperature': temperature
})
df.set_index('Date', inplace=True)
print("Sample Data:")
print(df.head())
# 2. Line plot - Temperature over time
plt.figure(figsize=(10, 4))
plt.plot(df.index, df['Temperature'], color='green')
plt.title('Monthly Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.tight_layout()
plt.show()
# 3. Rolling Average (Smoothing)
df['Rolling_Mean'] = df['Temperature'].rolling(window=12).mean()
plt.figure(figsize=(10, 4))
plt.plot(df['Temperature'], label='Actual', alpha=0.5)
plt.plot(df['Rolling_Mean'], label='12-Month Rolling Avg', color='red')
plt.title('Temperature with Rolling Average')
plt.legend()
plt.tight_layout()
plt.show()
# 4. Monthly Seasonality (Boxplot)
df['Month'] = df.index.month
plt.figure(figsize=(10, 5))
sns.boxplot(x='Month', y='Temperature', data=df)
plt.title('Seasonality by Month')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.tight_layout()
plt.show()
# 5. Heatmap of monthly averages (Year x Month)
df['Year'] = df.index.year
pivot_table = df.pivot_table(index='Year', columns='Month', values='Temperature')
plt.figure(figsize=(10, 5))
sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap='coolwarm')
plt.title('Monthly Avg Temperature (Heatmap)')
plt.xlabel('Month')
plt.ylabel('Year')
plt.tight_layout()
plt.show()

