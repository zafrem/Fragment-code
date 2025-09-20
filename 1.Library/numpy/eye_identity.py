import numpy as np

print("3x3 Identity Matrix using np.eye:")
eye_matrix = np.eye(3)
print(eye_matrix)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

print("3x4 Identity Matrix using np.eye:")
eye_matrix_non_square = np.eye(3, 4)
print(eye_matrix_non_square)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]]

print("3x3 Matrix with diagonal offset by 1 using np.eye (k=1):")
eye_matrix_k1 = np.eye(3, 3, k=1)
print(eye_matrix_k1)
# [[0. 1. 0.]
#  [0. 0. 1.]
#  [0. 0. 0.]]

print("4x4 Identity Matrix using np.identity:")
identity_matrix = np.identity(4)
print(identity_matrix)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]
