import numpy as np

linear_space = np.linspace(0, 10, 5)
print("Linear Space (0 to 10, 5 points):")
print(linear_space)

angles = np.linspace(0, 2 * np.pi, 100)
sin_values = np.sin(angles)

print("First 5 angles and their sine values:")
print(angles[:5])
print(sin_values[:5])

log_space = np.logspace(1, 3, 4)
print("Log Space (10^1 to 10^3, 4 points):")
print(log_space)

log_space_base2 = np.logspace(1, 10, num=10, base=2)
print("Log Space with base 2 (2^1 to 2^10, 10 points):")
print(log_space_base2)
