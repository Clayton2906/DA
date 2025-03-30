import pandas as pd


# Sample dataset
data = {'Values': [10, 20, 20, 30, 40, 50, None, 60, 70, 80, None]}
df = pd.DataFrame(data)

# Handling missing values (filling with mean)
df['Values'].fillna(df['Values'].mean(), inplace=True)
print("Hello")
# Descriptive statistics
mean = df['Values'].mean()
median = df['Values'].median()
mode = df['Values'].mode()[0]  # Mode can return multiple values, take the first one
variance = df['Values'].var()
std_dev = df['Values'].std()

# Print results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")

# Summary of the dataset
print("\nDataset Summary:")
print(df.describe())
