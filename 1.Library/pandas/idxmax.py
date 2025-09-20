import pandas as pd

data = {'City': ['Seoul', 'Busan', 'Incheon', 'Seoul', 'Busan']}
df = pd.DataFrame(data)
df_dummies = pd.get_dummies(df, columns=['City'])

print("one-hot encoding DataFrame:")
print(df_dummies)

df_reverted = df_dummies.idxmax(axis=1).str.replace('City_', '')

print("DataFrame Data:")
print(df_reverted)
