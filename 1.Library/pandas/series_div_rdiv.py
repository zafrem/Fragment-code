import pandas as pd

# Create a sample DataFrame
data = {
    'A': [10, 20, 30],
    'B': [40, 50, 60],
    'C': [70, 80, 90]
}
df = pd.DataFrame(data)

# Example of div() function
# Divide each element in the DataFrame by 10
result_div = df.div(10)
print("Result of div():")
print(result_div)

# Example of rdiv() function
# Divide 100 by each element in the DataFrame
result_rdiv = df.rdiv(100)
print("\nResult of rdiv():")
print(result_rdiv)
