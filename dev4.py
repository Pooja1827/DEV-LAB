import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Delhi': [14, 17, 23, 30, 34, 36, 34, 33, 31, 27, 21, 16],
    'Mumbai': [24, 25, 27, 29, 30, 29, 27, 27, 27, 28, 27, 25],
    'Chennai': [25, 26, 28, 31, 33, 34, 33, 33, 32, 30, 28, 26],
    'Kolkata': [18, 21, 26, 30, 32, 33, 32, 32, 31, 29, 24, 20]
}
df = pd.DataFrame(data)
df.set_index('Month', inplace=True)
print("Monthly Temperatures:\n", df)
plt.figure(figsize=(10, 5))
for city in df.columns:
    plt.plot(df.index, df[city], marker='o', label=city)
plt.title("City-wise Monthly Temperature (°C)")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
