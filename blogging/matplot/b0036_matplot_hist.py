import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
data = np.random.randn(1000)  # 평균이 0이고 표준편차가 1인 정규 분포를 따르는 1000개의 데이터

plt.hist(data, bins=30, alpha=0.75, edgecolor='black')
"""
data: The data to use for the histogram.
bins=30: Number of bins in the histogram.
alpha=0.75: Transparency of the bars.
edgecolor='black': Border color of the bars.
"""
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.grid(True)  # Add grid for better visualization
plt.show()
