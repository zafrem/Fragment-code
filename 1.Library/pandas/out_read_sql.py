import pandas as pd
# pip install sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

# 1. SQLAlchemy
engine = create_engine('sqlite:///example.db')

# 2. Table Create Insert
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

# 3. SQL select
query = "SELECT name, age FROM users WHERE age > 25"
df_query = pd.read_sql(query, con=engine)

# 4. 테이블 전체 읽기
df_table = pd.read_sql('users', con=engine)

# 5. 결과 출력
print("DataFrame from SQL query:")
print(df_query)

print("DataFrame from SQL table:")
print(df_table)
