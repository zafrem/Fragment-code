import matplotlib.pyplot as plt
import numpy as np

under_y = [-8, -6, -1, 5, 11, 17, 22, 22, 15, 8, 1, -6]
high_y = [2, 5, 11, 18, 23, 27, 29, 30, 26, 20, 12, 4]

x = ['January', 'February', 'March', 'April', 'May', 'June',
     'July', 'August', 'September', 'October', 'November', 'December' ]

plt.plot(x, under_y, 'ro--', label="High C°")
plt.plot(x, high_y, 'bo--', label="Low C°")

plt.xticks(rotation=-60)
plt.xlabel('Month')
plt.ylabel('C°')
plt.legend()

plt.show()