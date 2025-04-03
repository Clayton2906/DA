import pandas as pd

# Load dataset
file_path = r"C:\Users\angir\Downloads\worldcities.csv"
df = pd.read_csv(file_path)

# Check if "population" column exists before proceeding
if "population" in df.columns:
    # Compute Q1 (25th percentile) and Q3 (75th percentile)
    Q1 = df["population"].quantile(0.25)
    Q3 = df["population"].quantile(0.75)
    IQR = Q3 - Q1  # Interquartile Range

    # Define lower and upper bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Identify outliers
    outliers = df[(df["population"] < lower_bound) | (df["population"] > upper_bound)]
    print("\nDetected Outliers:\n", outliers)

    # Remove outliers
    df_cleaned = df[(df["population"] >= lower_bound) & (df["population"] <= upper_bound)]
    
    print("\nData after removing outliers:\n", df_cleaned.head())

    # Save the cleaned data
    df_cleaned.to_csv(r"C:\Users\angir\Downloads\worldcities_cleaned.csv", index=False)

else:
    print("Column 'population' not found in dataset.")
