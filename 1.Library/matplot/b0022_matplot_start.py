# pip install -U matplotlib

import numpy as np
import matplotlib.pyplot as plt

plt.title("Drawing Multi-Line Graphs")

x = [0, 1, 2, 3, 4, 5]
y = [1, 2, 4, 6, 8, 10]
plt.plot(x, y, '.-', color = 'black' , label = 'meaning')

t = np.arange(0., 5., 0.2) # [0., 0.2, 0.4, 0.6, ..., 4.6, 4.8]
plt.plot(t, t, '.--', label="linear", color='red')
plt.plot(t, t ** 2, 'o-.', label="square", color='blue')
plt.plot(t, t ** 3, '*:', label="cubic", color='green')

plt.xlabel('x-label')
plt.ylabel('y-label')

plt.axis([0, 5, 0, 20])
plt.legend()

plt.show()