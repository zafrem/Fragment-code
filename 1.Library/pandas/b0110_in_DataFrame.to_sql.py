import pandas as pd
# pip install sqlalchemy
from sqlalchemy import create_engine

# Step 1. SQLAlchemy Create
engine = create_engine('sqlite:///example.db')

# Step 2. Data
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'San Francisco', 'Los Angeles']
}
df = pd.DataFrame(data)

# Step 3. DataFrame to SQL
df.to_sql('users', con=engine, if_exists='replace', index=False)
print("DataFrame has been saved to the 'users' table.")

# etc. Read and Print
df_from_sql = pd.read_sql_table('users', con=engine)
print("DataFrame read from SQL:")
print(df_from_sql)
