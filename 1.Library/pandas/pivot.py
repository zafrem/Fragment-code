import pandas as pd

data = {
    'Name': ['Alice', 'Alice', 'Alice', 'Bob', 'Bob',
             'Bob', 'Charlie', 'Charlie', 'Charlie'],
    'Subject': ['Math', 'Science', 'English', 'Math',
                'Science', 'English', 'Math', 'Science', 'English'],
    'Score': [85, 88, 87, 90, 93, 89, 95, 97, 92]
}

df_long = pd.DataFrame(data)
print("Original DataFrame:")
print(df_long)

df_wide = df_long.pivot(index='Name', columns='Subject', values='Score')
# pivot() : Assumes that there are no duplicate values in the data.
#           If there are duplicate values, an error is thrown.
# pivot_table() : When there are duplicate values,
#           you can use the aggregation function (aggfunc) to handle them.

print("Pivoted DataFrame:")
print(df_wide)
