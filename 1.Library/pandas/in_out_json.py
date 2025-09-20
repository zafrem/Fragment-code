import pandas as pd
import io
from pandas.io.json import build_table_schema

json_data = '''
[
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "Los Angeles"}
]
'''
df = pd.read_json(io.StringIO(json_data))
print("DataFrame from JSON:")
print(df)

nested_json = [
    {
        "name": "Alice",
        "info": {"age": 25, "city": "New York"},
        "scores": [100, 90]
    },
    {
        "name": "Bob",
        "info": {"age": 30, "city": "San Francisco"},
        "scores": [85, 88]
    }
]

df_normalized = pd.json_normalize(nested_json, sep='_')
print("Normalized DataFrame:")
print(df_normalized)

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "San Francisco", "Los Angeles"]
})
json_result = df.to_json(orient="records", indent=2)
print("DataFrame to JSON:")
print(json_result)

schema = build_table_schema(df)
print("DataFrame Schema:")
print(schema)
