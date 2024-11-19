import pandas as pd

data = {'City': ['Seoul', 'Busan', 'Incheon', 'Seoul', 'Busan', 'Daegu']}
df = pd.DataFrame(data)

print("Org Data:")
print(df)

labels, unique = pd.factorize(df['City'])
# pandas.factorize(values, sort=False, na_sentinel=-1, size_hint=None)
# values: The data to convert (Series, DataFrame, etc.).
# sort: Return labels sorted if set to True (defaults to False).
# na_sentinel: The label to specify for missing values (defaults to -1).
df['City_encoded'] = labels

print("Encode Data:")
print(df)

print("Unique Label:")
print(unique)
