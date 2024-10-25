import pandas as pd

df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value': [1, 2, 3, 4]
})

df2 = pd.DataFrame({
    'key': ['B', 'D', 'E', 'F'],
    'value': [5, 6, 7, 8]
})

# merge example
merged_df = pd.merge(df1, df2, on='key', how='inner', suffixes=('_df1', '_df2'))
print("Merge Example:\n", merged_df)

df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [1, 2, 3],
    'date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03'])
})

df2 = pd.DataFrame({
    'key': ['B', 'C', 'D'],
    'value2': [4, 5, 6],
    'date': pd.to_datetime(['2024-01-02', '2024-01-04', '2024-01-05'])
})

# merge_ordered example
ordered_merged_df = pd.merge_ordered(df1, df2, on='date', fill_method='ffill')
print("\nMerge Ordered Example:\n", ordered_merged_df)

df1 = pd.DataFrame({
    'date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04']),
    'price': [100, 101, 102, 103]
})

df2 = pd.DataFrame({
    'date': pd.to_datetime(['2024-01-01', '2024-01-03']),
    'event': ['Earnings', 'Dividend']
})

# merge_asof example
asof_merged_df = pd.merge_asof(df1, df2, on='date')
print("\nMerge Asof Example:\n", asof_merged_df)
