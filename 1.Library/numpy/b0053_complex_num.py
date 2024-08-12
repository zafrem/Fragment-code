import numpy as np

arr_complex = np.array([1+2j, 3+4j, 5+6j])
print("[Complex Array]")
print(arr_complex)
print("Real Part:", arr_complex.real)
print("Imaginary Part:", arr_complex.imag)

# [Complex Array]
# [1.+2.j 3.+4.j 5.+6.j]
# Real Part: [1. 3. 5.]
# Imaginary Part: [2. 4. 6.]