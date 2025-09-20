import pandas as pd

data1 = {'A': [1, 2], 'B': [3, 4]}
data2 = {'A': [5, 6], 'B': [7, 8]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

df_concat_row = pd.concat([df1, df2])
print("row :")
print(df_concat_row)

df_concat_col = pd.concat([df1, df2], axis=1)
print("\ncol :")
print(df_concat_col)

df_concat_ignore_index = pd.concat([df1, df2], ignore_index=True)
print("\nignore_index=True 설정:")
print(df_concat_ignore_index)