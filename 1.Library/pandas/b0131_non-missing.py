import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', np.nan, 'David', 'Eve'],
    'Age': [24, np.nan, 30, 22, np.nan],
    'City': ['Seoul', 'Busan', 'Incheon', np.nan, 'Daegu']
}
df = pd.DataFrame(data)

print("Ord data:")
print(df)

print("Check for missing values (isna):")
print(df.isna())

print("Check for missing values (isnull):")
print(df.isnull())

print("Check for non-missing values (notna):")
print(df.notna())

print("Check for non-missing values (notnull):")
print(df.notnull())
