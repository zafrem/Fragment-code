import numpy as np

print("[Integer Array]")
arr_int = np.array([1, 2, 3, 4, 5])
print(arr_int)
print("Data Type:", arr_int.dtype)
# int64

print("[Float Array]")
arr_float = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
print(arr_float)
print("Data Type:", arr_float.dtype)
# float64

print("[Complex Array]")
arr_complex = np.array([1+2j, 3+4j, 5+6j])
print(arr_complex)
print("Data Type:", arr_complex.dtype)
# complex128

print("[Converted Float Array to Integer Array]")
arr_float_to_int = arr_float.astype(int)
print(arr_float_to_int)
print("Data Type:", arr_float_to_int.dtype)
# int64

print("[Mixed Data Type Array]")
arr_mixed = np.array([1, 2.2, 3+3j, True], dtype=object)
print(arr_mixed)
print("Data Type:", arr_mixed.dtype)
# object

print("[Explicit Data Type Array] (Float64)")
arr_explicit_dtype = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(arr_explicit_dtype)
print("Data Type:", arr_explicit_dtype.dtype)
# float64
