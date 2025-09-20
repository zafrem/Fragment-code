import pandas as pd

data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'score_2021': [85, 78, 92],
    'score_2022': [88, 79, 94],
    'score_2023': [90, 80, 96]
}
df = pd.DataFrame(data)

print("org (wide):")
print(df)

df_long = pd.wide_to_long(df, stubnames='score', i='id', j='year', sep='_', suffix='\\d+')
# pandas.wide_to_long(df, stubnames, i, j, sep='', suffix='\\d+')
# df: The data frame to convert.
# stubnames: Prefixes that are common to multiple columns.
# i: Column names to use as indexes (e.g., individual identifiers).
# j: The name of the delimiter variable in “long” format that will be created.
# sep: Separator between the prefix and the number in the column name.
# suffix: A pattern of numbers or identifiers following the prefix.
print("change (long):")
print(df_long.reset_index())
