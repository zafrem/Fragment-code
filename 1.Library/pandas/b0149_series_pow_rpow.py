import pandas as pd

# Create a sample DataFrame
data = {
    'A': [2, 3, 4],
    'B': [5, 6, 7],
    'C': [8, 9, 10]
}
df = pd.DataFrame(data)

# Raise each element in the DataFrame to the power of 2
result_pow = df.pow(2)
print("Result of pow():")
print(result_pow)

# Raise 2 to the power of each element in the DataFrame
result_rpow = df.rpow(2)
print("\nResult of rpow():")
print(result_rpow)
