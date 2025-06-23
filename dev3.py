# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Working with NumPy Arrays
# -----------------------------

# Create a 1D NumPy array
array_1d = np.array([10, 20, 30, 40, 50])
print("1D Array:", array_1d)

# Create a 2D NumPy array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", array_2d)

# Perform basic operations on the array
print("\nSum of 1D Array:", array_1d.sum())
print("Mean of 1D Array:", array_1d.mean())
print("Shape of 2D Array:", array_2d.shape)

# -----------------------------
# Step 2: Working with Pandas DataFrame
# -----------------------------

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Score': [85, 62, 90, 70]
}
df = pd.DataFrame(data)

# Display the DataFrame
print("\nDataFrame:\n", df)

# Calculate the average score
average_score = df['Score'].mean()
print("\nAverage Score:", average_score)

# Filter students with Age > 25
filtered_df = df[df['Age'] > 25]
print("\nStudents with Age > 25:\n", filtered_df)

# -----------------------------
# Step 3: Basic Plots using Matplotlib
# -----------------------------

# Line plot of Scores
plt.figure(figsize=(8, 4))
plt.plot(df['Name'], df['Score'], marker='o', color='blue', linestyle='--')
plt.title('Scores of Students')
plt.xlabel('Name')
plt.ylabel('Score')
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar plot of Age
plt.figure(figsize=(8, 4))
plt.bar(df['Name'], df['Age'], color='green')
plt.title('Age of Students')
plt.xlabel('Name')
plt.ylabel('Age')
plt.tight_layout()
plt.show()
