import pandas as pd

data = {
    'Name': ['Alice', 'Bob'],
    'Score_1': [85, 75],
    'Score_2': [90, 80],
    'Score_3': [88, 79]
}
df = pd.DataFrame(data)

print("Org DataFrame:")
print(df)

long_df = pd.lreshape(df, {'Score': ['Score_1', 'Score_2', 'Score_3']})

print("Deformed data frame (convert to long form):")
print(long_df)
