import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Department': ['HR', 'IT', 'Sales', 'Marketing', 'Finance'],
    'Total_Hours': [1200, 2200, 1800, 1500, 1600]
}
df = pd.DataFrame(data)
print("Work Hours by Department:\n", df)
plt.figure(figsize=(8, 4))
plt.bar(df['Department'], df['Total_Hours'], color='skyblue')
plt.title("Department-wise Total Work Hours")
plt.xlabel("Department")
plt.ylabel("Total Hours Worked")
plt.grid(axis='y')
plt.tight_layout()
plt.show()
plt.figure(figsize=(6, 6))
plt.pie(df['Total_Hours'], labels=df['Department'], autopct='%1.1f%%', startangle=90)
plt.title("Work Hour Distribution by Department")
plt.tight_layout()
plt.show()
