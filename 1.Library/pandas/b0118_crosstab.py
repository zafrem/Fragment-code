import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice',
             'Bob', 'Charlie', 'Alice', 'Bob',
             'Charlie', 'Alice', 'Bob'],
    'Subject': ['Math', 'Math', 'Math', 'Science',
                'Science', 'Science', 'English', 'English',
                'English', 'Math', 'Science'],
    'Passed': [True, False, True, True,
               False, True, False, True,
               False, True, True]
}

df = pd.DataFrame(data)

crosstab_result = pd.crosstab(df['Name'], df['Passed'])

print("Crosstab Result:")
print(crosstab_result)
