import numpy as np

# 예제 행렬 생성
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# SVD 수행
U, S, Vt = np.linalg.svd(A)

print("Matrix U (Left singular vectors)")
print(U)
print("Singular Values (S):")
print(S)
print("Matrix Vt (Right singular vectors, transposed)")
print(Vt)

Sigma = np.zeros((A.shape[0], A.shape[1]))
Sigma[:len(S), :len(S)] = np.diag(S)

A_reconstructed = np.dot(U, np.dot(Sigma, Vt))

print("Reconstructed Matrix A from U, S, Vt:")
print(A_reconstructed)
