import pandas as pd

data = [10, 20, 30, 40, 50]
index_labels = ['a', 'b', 'c', 'd', 'e']
series = pd.Series(data, index=index_labels)

print("Create Series:")
print(series)

df = series.to_frame(name='Values')

df.to_csv('output_series.csv', index=True)
