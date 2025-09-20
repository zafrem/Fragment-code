import pandas as pd

data = {'City': ['Seoul', 'Busan', 'Incheon', 'Seoul', 'Busan']}
df = pd.DataFrame(data)

print("Org DataFrame:")
print(df)

df_dummies = pd.get_dummies(df, columns=['City'])
print("one-hot encoding DataFrame:")
print(df_dummies)

df_dummies_drop = pd.get_dummies(df, columns=['City'], drop_first=True)
print("Multicollinearity (drop_first=True):")
print(df_dummies_drop)
