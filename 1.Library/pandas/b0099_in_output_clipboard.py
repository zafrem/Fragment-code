# Clipboard -> Code (read_clipboard)
"""
col1\tcol2\tcol3
1\t2\t3
4\t5\t6
7\t8\t9
"""

import pandas as pd

df_clipboard = pd.read_clipboard()
print("DataFrame read from clipboard:")
print(df_clipboard)

# Code -> Clipboard (DataFrame.to_clipboard)
df = pd.DataFrame({
    'col1': [1, 4, 7],
    'col2': [2, 5, 8],
    'col3': [3, 6, 9]
})

df.to_clipboard(index=False)
print("\nDataFrame copied to clipboard.")
