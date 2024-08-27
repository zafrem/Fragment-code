import numpy as np

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

variance = np.var(data)
print("Variance of the data:", variance)

standard_deviation = np.std(data)
print("Standard Deviation of the data:", standard_deviation)

data_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

variance_2d = np.var(data_2d)
std_2d = np.std(data_2d)

print("Variance of the 2D data:", variance_2d)
print("Standard Deviation of the 2D data:", std_2d)

variance_along_axis0 = np.var(data_2d, axis=0)
std_along_axis0 = np.std(data_2d, axis=0)

print("Variance along axis 0:", variance_along_axis0)
print("Standard Deviation along axis 0:", std_along_axis0)

variance_along_axis1 = np.var(data_2d, axis=1)
std_along_axis1 = np.std(data_2d, axis=1)

print("Variance along axis 1:", variance_along_axis1)
print("Standard Deviation along axis 1:", std_along_axis1)
