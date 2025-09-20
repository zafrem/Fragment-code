import pandas as pd

# Create a Series with float values
series = pd.Series([3.14159, 2.71828, 1.61803])

# Round to 2 decimal places
rounded_series = series.round(2)

print("Original Series:")
print(series)

print("\nRounded Series:")
print(rounded_series)

# Create a DataFrame with float values
data = {
    'A': [1.2345, 2.3456, 3.4567],
    'B': [4.5678, 5.6789, 6.7890]
}
df = pd.DataFrame(data)

# Round all columns to 1 decimal place
rounded_df = df.round(1)

print("Original DataFrame:")
print(df)

print("\nRounded DataFrame:")
print(rounded_df)


# Create a DataFrame with float values
data = {
    'A': [1.2345, 2.3456, 3.4567],
    'B': [4.5678, 5.6789, 6.7890]
}
df = pd.DataFrame(data)

# Specify rounding for each column
rounded_df = df.round({'A': 2, 'B': 0})

print("Column-Specific Rounding:")
print(rounded_df)
