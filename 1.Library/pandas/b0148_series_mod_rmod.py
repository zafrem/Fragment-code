import pandas as pd

# Create a sample DataFrame
data = {
    'A': [10, 15, 20],
    'B': [25, 30, 35],
    'C': [40, 45, 50]
}
df = pd.DataFrame(data)

# Example of mod() function
# Compute the modulo of each element in the DataFrame by 7
result_mod = df.mod(7)
print("Result of mod():")
print(result_mod)

# Example of rmod() function
# Compute the modulo of 50 by each element in the DataFrame
result_rmod = df.rmod(50)
print("\nResult of rmod():")
print(result_rmod)
