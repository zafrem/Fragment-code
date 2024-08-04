import matplotlib.pyplot as plt

#  Data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
colors = [80, 40, 10, 50, 60]
sizes = [100, 900, 2000, 1000, 1600]

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.colorbar()

plt.title('Scatter Plot with Colors and Sizes')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()
