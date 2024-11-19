import numpy as np

a = np.arange(6)
print(a) # [0 1 2 3 4 5]
b = a.reshape((2, 3))
print(b) # [[0 1 2] [3 4 5]]

a = np.array([[1, 2, 3], [4, 5, 6]])
t = np.transpose(a)
print(t)
# [[1 4]
# [2 5]
# [3 6]]

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.concatenate((a, b))
print(c) # [1 2 3 4 5 6]

v = np.vstack((a, b))
print(v)
# [[1 2 3]
# [4 5 6]]

h = np.hstack((a, b))
print(h) # [1 2 3 4 5 6]

a = np.array([1, 2, 2, 3, 3, 3])
unique_elements = np.unique(a)
print(unique_elements) # [1 2 3]

a = np.array([1, 2, 3, 4, 5])
indices = np.where(a > 3)
print(indices) # (array([3, 4]),)

rand = np.random.rand(3, 3)
print(rand)
# [[0.84776263 0.91780585 0.00408862]
# [0.22736669 0.7148289 0.58207966]
# [0.68171305 0.17723367 0.88789426]