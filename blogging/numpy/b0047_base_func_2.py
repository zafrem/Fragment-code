import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.add(a, b)
print(result) # [5 7 9]

result = np.subtract(a, b)
print(result) # [-3 -3 -3]

result = np.multiply(a, b)
print(result) # [ 4 10 18]

result = np.divide(a, b)
print(result) # [0.25 0.4  0.5 ]

m = np.mean(a)
print(m) # 2.0

med = np.median(a)
print(med) # 2.0

s = np.std(a)
print(s) # 0.816496580927726

s = np.sum(a)
print(s) # 6

min_val = np.min(a)
print(min_val) # 1

max_val = np.max(a)
print(max_val) # 3

