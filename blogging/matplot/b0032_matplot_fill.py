import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.fill_between(x, y1, y2, color='orange', alpha=0.5)

plt.plot(x, y1, color='blue', label='sin(x)')
plt.plot(x, y2, color='green', label='cos(x)')

plt.title('Fill Between Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()

plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)

plt.fill_between(x, y1, color='purple', alpha=0.5, where=(y1 > 0), label='y1 > 0')
plt.fill_between(x, y1, color='red', alpha=0.5, where=(y1 <= 0), label='y1 <= 0')

plt.plot(x, y1, color='black')

plt.title('Fill Between Axis Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()

plt.show()
