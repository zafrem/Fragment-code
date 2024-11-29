import pandas as pd

# Create a DataFrame
data = {
    'A': [10, 20, 30],
    'B': [5, 25, 35],
    'C': [15, 10, 40]
}
df = pd.DataFrame(data)

# Compare each element to 20
lt_result = df.lt(20)  # Less than 20
gt_result = df.gt(20)  # Greater than 20

print("Original DataFrame:")
print(df)

print("\nResult of lt (less than 20):")
print(lt_result)

print("\nResult of gt (greater than 20):")
print(gt_result)


# Create another DataFrame
df2 = pd.DataFrame({
    'A': [15, 10, 25],
    'B': [5, 30, 20],
    'C': [20, 10, 35]
})

# Compare two DataFrames
lt_result = df.lt(df2)  # Element-wise less than
gt_result = df.gt(df2)  # Element-wise greater than

print("\nSecond DataFrame:")
print(df2)

print("\nResult of lt (df < df2):")
print(lt_result)

print("\nResult of gt (df > df2):")
print(gt_result)


# filtered_df = df[df.lt(20)]
