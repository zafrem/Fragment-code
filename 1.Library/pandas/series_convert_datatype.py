import pandas as pd

# to_numpy()
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
print("Org DataFrame:")
print(df)
array = df.to_numpy()
print("Numpy Array :")
print(array)

# to_period()
dates = pd.Series(pd.date_range('2024-01-01', periods=4))
print("Org Date :")
print(dates)
periods = dates.dt.to_period('M')
print("Period Date :")
print(periods)

# to_timestamp()
periods = pd.Series(pd.period_range('2024-01', periods=4, freq='M'))
print("Org Period Data :")
print(periods)
timestamps = periods.dt.to_timestamp()
print("Timestamp로 Data :")
print(timestamps)

# to_list()
data = pd.Series([10, 20, 30, 40])
print("Org Series :")
print(data)
data_list = data.to_list()
print("List Data :")
print(data_list)
