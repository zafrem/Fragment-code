import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 20, 15, 25, 20, 15, 5, 20, 23, 30]

plt.step(x, y, where='mid')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Step Plot Example')
plt.show()