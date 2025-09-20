import pandas as pd

data = {
    'Name': ['Alice', 'Alice', 'Alice', 'Bob', 'Bob',
             'Bob', 'Charlie', 'Charlie', 'Charlie'],
    'Subject': ['Math', 'Science', 'English', 'Math', 'Science',
                'English', 'Math', 'Science', 'English'],
    'Score': [85, 88, 87, 90, 93, 89, 95, 97, 92],
    'Attempts': [1, 2, 1, 2, 2, 1, 1, 2, 2]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

df_pivot = pd.pivot_table(df,
                          index='Name',
                          columns='Subject',
                          values='Score',
                          aggfunc='mean',
                          margins=True)
# index: The column to use as rows in the pivot table.
# columns: The columns to use as columns in the pivot table.
# values: The columns with values to display in the pivot table.
# aggfunc: The aggregation function. The default is set to mean,
#        which calculates the average over duplicate values.
#        Other aggregation functions include sum, count, min, max, etc.
# margins: If set to True, adds the total of each row and column.
print("Pivot Table (Average Scores):")
print(df_pivot)
