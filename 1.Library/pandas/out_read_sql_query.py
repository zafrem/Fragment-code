import pandas as pd
# pip install sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

# 1. SQLAlchemy SQLite
engine = create_engine('sqlite:///example.db')

# 2. Table Create & Insert
metadata = MetaData()
users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String),
                    Column('age', Integer),
                    Column('city', String))

metadata.create_all(engine)
with engine.connect() as conn:
    conn.execute(users_table.insert(), [
        {'name': 'Alice', 'age': 25, 'city': 'New York'},
        {'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
        {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles'}
    ])
    conn.commit()

# 3. SQL Query (Select)
query = "SELECT name, age FROM users WHERE age > 25"
df = pd.read_sql_query(query, con=engine)

print("DataFrame from SQL query:")
print(df)

