import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')

for i, txt in enumerate(['A', 'B', 'C', 'D', 'E']):
    plt.text(x[i], y[i], txt, fontsize=12, rotation=-5)

plt.title('Multiple Text Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()


