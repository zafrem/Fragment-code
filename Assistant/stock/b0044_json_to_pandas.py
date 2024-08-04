import json
import pandas as pd
import datetime

with open("b0044_AAPL_2406.json", "r") as fp_json:
    aapl_2406_data = json.load(fp_json)

pd_tmp_data = []

for _date in aapl_2406_data["Time Series (5min)"]:
    tmp_data = aapl_2406_data["Time Series (5min)"][_date]
    pd_tmp_data.append([datetime.datetime.strptime(_date, '%Y-%m-%d %H:%M:%S'), float(tmp_data['open']),
                        float(tmp_data['high']), float(tmp_data['low']), float(tmp_data['close']),
                        float(tmp_data['volume'])])
df = pd.DataFrame(pd_tmp_data, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
print(df)
"""
[output]
                   date    open    high     low    close   volume
0    2024-06-28 19:55:00  211.41  211.70  211.40  211.660  13341.0
1    2024-06-28 19:50:00  211.31  211.44  211.31  211.440   4606.0
...                  ...     ...     ...     ...      ...      ...
3646 2024-06-03 04:05:00  193.10  193.31  192.90  192.900  14845.0
3647 2024-06-03 04:00:00  192.45  193.14  192.45  193.050  26584.0
"""
print(df.median())
"""
[output]
[3648 rows x 6 columns]
open        209.780
high        209.940
low         209.545
close       209.780
volume    26344.500
"""
"""
pandas.DataFreame.median()
axis: The axis on which to base the {0: index/1: columns} calculation.
skipna : Whether to ignore missing values.
level : For Multi Index, the level at which to perform the calculation.
numeric_only: Whether to use only numbers, decimals, and booleans.
kwargs : Additional keywords to pass to the function.
"""