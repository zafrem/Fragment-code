import numpy as np

a = np.array([1, 2, 3])
print(a) #[1 2 3]

z = np.zeros((3, 4)) # 0 init
print(z)
#[[0. 0. 0. 0.]
# [0. 0. 0. 0.]
# [0. 0. 0. 0.]]

o = np.ones((2, 3)) # 1 initå
print(o)
#[[1. 1. 1.]
# [1. 1. 1.]]

e = np.empty((2, 2)) # non-init
print(e)
#[[1.5e-323 4.0e-323]
# [4.0e-323 4.0e-323]]

ar = np.arange(10)
print(ar) # [0 1 2 3 4 5 6 7 8 9]

ar_step = np.arange(0, 10, 2)
print(ar_step) # [0 2 4 6 8]

lin = np.linspace(0, 1, 5)
print(lin) # [0.   0.25 0.5  0.75 1.  ]
