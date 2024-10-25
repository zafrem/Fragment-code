import pandas as pd

# pip install openpyxl

# Read Excel
df_sheets = pd.read_excel('examples.xlsx', sheet_name=['Sheet1', 'Sheet2']) # sheet_name is option
print("Data from multiple sheets:")
for sheet_name, df in df_sheets.items():
    print(f"Data from {sheet_name}:")
    print(df)

# Data
df = pd.DataFrame({
    'col1': [1, 2, 3],
    'col2': [4, 5, 6],
    'col3': [7, 8, 9]
})
df2 = pd.DataFrame({
    'A': [10, 11, 12],
    'B': [13, 14, 15]
})

print("DataFrame saved to 'example.xlsx'")
df.to_excel('example.xlsx', index=False)

print("DataFrame saved to 'example.xlsx' with multiple sheets")
with pd.ExcelWriter('examples.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)

