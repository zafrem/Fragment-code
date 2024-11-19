import pandas as pd

# Create a sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Example of mul() function
# Multiply each element in the DataFrame by 2
result_mul = df.mul(2)
print("Result of mul():")
print(result_mul)

# Example of rmul() function
# Multiply 10 by each element in the DataFrame
result_rmul = df.rmul(10)
print("\nResult of rmul():")
print(result_rmul)
