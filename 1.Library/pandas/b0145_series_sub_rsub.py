import pandas as pd

data = {
    'A': [10, 20, 30],
    'B': [40, 50, 60],
    'C': [70, 80, 90]
}
df = pd.DataFrame(data)

result_sub = df.sub(5)
print("sub() result:")
print(result_sub)

result_rsub = df.rsub(100)
print("\nrsub() result:")
print(result_rsub)
