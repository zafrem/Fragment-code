import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
data1 = np.random.rand(100) * 10
data2 = np.random.rand(100) * 10

plt.figure(figsize=(10, 6))
plt.eventplot([data1, data2], colors=['b', 'g'])
plt.xlabel('Event Position')
plt.ylabel('Event Type')
plt.title('Event Plot Example')
plt.grid(True)  # Add grid for better visualization
plt.show()
