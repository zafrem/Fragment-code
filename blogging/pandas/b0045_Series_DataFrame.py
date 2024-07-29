import pandas as pd


# Series: a one-dimensional labeled array
s = pd.Series([1, 3, 5, 7, 9])
print(s)
"""
output
0    1
1    3
2    5
3    7
4    9
dtype: int64
"""
# DataFrame: a two-dimensional data structure
df = pd.DataFrame(data=[1, 3, 5, 7, 9], index=range(0,5), columns=['A'])
print(df)
"""
output
  A
0  1
1  3
2  5
3  7
4  9
"""
dates = pd.date_range("20130101", periods=6)
pd.DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
df = pd.DataFrame([[1,2,3,4],[5,6,7,8],[],[],[],[]], index=dates, columns=list("ABCD"))
print(df)
"""
output
              A    B    C    D
2013-01-01  1.0  2.0  3.0  4.0
2013-01-02  5.0  6.0  7.0  8.0
2013-01-03  NaN  NaN  NaN  NaN
2013-01-04  NaN  NaN  NaN  NaN
2013-01-05  NaN  NaN  NaN  NaN
2013-01-06  NaN  NaN  NaN  NaN
"""


