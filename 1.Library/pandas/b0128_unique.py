import pandas as pd

data = {'City': ['Seoul', 'Busan', 'Incheon', 'Seoul', 'Busan', 'Daegu']}
df = pd.DataFrame(data)

print("Org Data:")
print(df)

unique_cities = pd.unique(df['City'])

print("\nUnique City:")
print(unique_cities)
