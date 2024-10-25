import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 90, 95],
    'Science': [88, 93, 97],
    'English': [87, 89, 92]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

df_melted = pd.melt(df, id_vars=['Name'],
                    value_vars=['Math', 'Science', 'English'],
                    var_name='Subject', value_name='Score')
# id_vars: The columns you want to keep.
# value_vars: Specifies the columns you want to convert to long form.
# var_name: The name of the converted column.
# value_name: The name of the converted value.

print("Melted DataFrame:")
print(df_melted)
