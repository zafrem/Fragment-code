import pandas as pd

data = [10, 5, 30]
index_labels = ['a', 'b', 'c']
series = pd.Series(data, index=index_labels)

print("Org Series:")
print(series)

# Data add
series['e'] = 40

print("Add Series:")
print(series)

# Data drop
series = series.drop('b')

print("Drop Series:")
print(series)

# Value Sort
sorted_by_value = series.sort_values()

print("Value Sort Series:")
print(sorted_by_value)

# Index Sort
sorted_by_index = series.sort_index()

print("Index Sort Series:")
print(sorted_by_index)
