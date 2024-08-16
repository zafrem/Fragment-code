import numpy as np

arr = np.array([1, np.e, np.e**2, 10])
natural_log = np.log(arr)

print("Original Array:")
print(arr)

print("Natural Log (log base e):")
print(natural_log)

print("Log base 2:")
log2_result = np.log2(arr)
print(log2_result)

print("Log base 10:")
log10_result = np.log10(arr)
print(log10_result)

print("Original Array:")
exp_arr = np.array([0, 1, 2, 3])
exponential = np.exp(exp_arr)
print(exp_arr)

print("Exponential (e^x):")
print(exponential)
