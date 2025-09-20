import pandas as pd

series1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
series2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])

print("Series1 :")
print(series1)

print("Series2 :")
print(series2)

result = series1.add(series2, fill_value=0)

print("Series1 + Series2 :")
print(result)

# radd
series3 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
series4 = pd.Series([5, 15], index=['b', 'd'])

print("Series3 :")
print(series3)

print("Series4 :")
print(series4)

result_radd = series4.radd(series3, fill_value=0)

print("Series3 + Series4(revers):")
print(result_radd)
