# Step 1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the dataset
df = pd.read_csv('sms_sample.csv')  # Use full path if not in same folder

# Step 3: Show first few rows
print("📌 First 5 rows of the dataset:")
print(df.head())

# Step 4: Rename columns for clarity (if needed)
df.columns = ['label', 'message']  # Already labeled, but ensuring clarity

# Step 5: Check basic information
print("\n📌 Dataset Info:")
print(df.info())

# Step 6: Check for missing values
print("\n📌 Missing values:")
print(df.isnull().sum())

# Step 7: Check class distribution
print("\n📌 Class distribution:")
print(df['label'].value_counts())

# Step 8: Add a new column for message length
df['message_length'] = df['message'].apply(len)

# Step 9: Display descriptive statistics
print("\n📌 Descriptive Statistics:")
print(df.describe())

# Step 10: Plot class distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='label', palette='Set2')
plt.title("Spam vs Ham Distribution")
plt.xlabel("Label")
plt.ylabel("Count")
plt.grid(True, axis='y')
plt.show()

# Step 11: Plot histogram of message lengths
plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='message_length', bins=10, kde=True)
plt.title("Distribution of Message Lengths")
plt.xlabel("Message Length")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Step 12: Box plot to compare message length by label
plt.figure(figsize=(8, 5))
sns.boxplot(x='label', y='message_length', data=df, palette='coolwarm')
plt.title("Message Length by Label")
plt.show()
