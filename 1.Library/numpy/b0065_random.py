import numpy as np

random_array = np.random.random(5)
print("Random Array [0.0, 1.0):")
print(random_array)

random_array_2d = np.random.random((3, 3))
print("2D Random Array [0.0, 1.0):")
print(random_array_2d)

rand_array = np.random.rand(5)
print("Rand Array [0.0, 1.0):")
print(rand_array)

rand_array_2d = np.random.rand(3, 3)
print("2D Rand Array [0.0, 1.0):")
print(rand_array_2d)

randint_array = np.random.randint(1, 10, 5)
print("Randint Array [1, 10):")
print(randint_array)

randint_array_2d = np.random.randint(1, 10, (3, 3))
print("2D Randint Array [1, 10):")
print(randint_array_2d)

random_integers_array = np.random.randint(1, 10, 5)
print("Random Integers Array [1, 10]:")
print(random_integers_array)

random_integers_array_2d = np.random.randint(1, 10, (3, 3))
print("2D Random Integers Array [1, 10]:")
print(random_integers_array_2d)

randn_array = np.random.randn(5)
print("Randn Array (Standard Normal Distribution):")
print(randn_array)

randn_array_2d = np.random.randn(3, 3)
print("2D Randn Array (Standard Normal Distribution):")
print(randn_array_2d)