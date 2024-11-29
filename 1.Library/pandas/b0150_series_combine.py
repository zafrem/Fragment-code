import pandas as pd

# Create two Series
series1 = pd.Series([1, 2, 3, 4])
series2 = pd.Series([10, 20, 30, 40])

# Use combine to find the maximum value element-wise
result = series1.combine(series2, func=max)

print("Result of combine with Series:")
print(result)


