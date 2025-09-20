import pandas as pd
import numpy

data = ['apple', 'banana', 'cherry', 'apple', 'banana']
series = pd.Series(data)

print("Org Series:")
print(series)

hash_values = pd.util.hash_pandas_object(series)
# pandas.util.hash_pandas_object(obj, index=True, encoding='utf8',
#                   hash_key='0123456789123456', categorize=True)
# obj : Index, Series, or DataFrame
# index : bool, default True
# encoding : str, default ‘utf8’
# hash_key : str, default _default_hash_key
# categorize : bool, default True
print("Hash value:")
print(hash_values)
