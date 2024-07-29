import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]
colors = ['red', 'blue', 'green', 'purple', 'orange']

plt.bar(categories, values, color=colors)

plt.title('Basic Bar Chart with Colors')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.show()

#Horizontal Bar
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]

plt.barh(categories, values)

plt.title('Horizontal Bar Chart')
plt.xlabel('Values')
plt.ylabel('Categories')

plt.show()

# Multiple Bar
import matplotlib.pyplot as plt
import numpy as np

categories = ['A', 'B', 'C', 'D', 'E']
values1 = [5, 7, 3, 8, 6]
values2 = [4, 6, 2, 7, 5]

bar_width = 0.35
index = np.arange(len(categories))

plt.bar(index, values1, bar_width, label='Series 1', color='blue')
plt.bar(index + bar_width, values2, bar_width, label='Series 2', color='green')

plt.title('Multiple Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.xticks(index + bar_width / 2, categories)

plt.legend()

plt.show()

#Stacked Bar
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values1 = [5, 7, 3, 8, 6]
values2 = [4, 6, 2, 7, 5]

plt.bar(categories, values1, label='Series 1', color='blue')
plt.bar(categories, values2, bottom=values1, label='Series 2', color='green')

plt.title('Stacked Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.legend()

plt.show()
