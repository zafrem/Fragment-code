import pandas as pd
import numpy as np

data = np.random.randn(10) * 10
print("Original Data:\n", data)

bins = [-np.inf, -5, 5, np.inf]
labels = ['Low', 'Medium', 'High']
categorized_data = pd.cut(data, bins=bins, labels=labels)
print("\nCategorized Data (cut):\n", categorized_data)

quantile_categorized = pd.qcut(data, q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
print("\nQuantile Categorized Data (qcut):\n", quantile_categorized)
