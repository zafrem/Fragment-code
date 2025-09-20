import pandas as pd
# pip install sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

engine = create_engine('sqlite:///example.db')

#      name    age        city
# 0    Alice    25       New York
# 1    Bob      30     San Francisco
# 2    Charlie  35      Los Angeles

df = pd.read_sql_table('users', con=engine)
print(df)

metadata = MetaData()
users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String),
                    Column('age', Integer),
                    Column('city', String))

metadata.create_all(engine)

# Insert
with engine.connect() as conn:
    conn.execute(users_table.insert(), [
        {'name': 'Alice_2', 'age': 35, 'city': 'in USA'},
        {'name': 'Bob_2', 'age': 40, 'city': 'in UK'},
        {'name': 'Charlie_2', 'age': 45, 'city': 'in Canada'}
    ])
    conn.commit()
print("Data inserted into users table.")

df_from_sql = pd.read_sql_table('users', con=engine)
print("DataFrame read from SQL:")
print(df_from_sql)