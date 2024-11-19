import pandas as pd

print("[Numeric]")

data = {'values': ['10', '20', '30', 'invalid', '50']}
df = pd.DataFrame(data)

print("Org data:")
print(df)

df['values_numeric'] = pd.to_numeric(df['values'], errors='coerce')
print("Numeric data:")
print(df)

print("[Datatime]")

data = {'dates': ['2023-01-01', '2023-05-15', '2024/07/20', 'invalid']}
df = pd.DataFrame(data)

print("Org data:")
print(df)

df['dates_datetime'] = pd.to_datetime(df['dates'], errors='coerce')
print("Datetime data:")
print(df)

print("[Timedelta]")

data = {'duration': ['5 days', '10 days', '15 hours', 'invalid']}
df = pd.DataFrame(data)

print("Org Data:")
print(df)

df['duration_timedelta'] = pd.to_timedelta(df['duration'], errors='coerce')
print("Timedelta Data:")
print(df)
