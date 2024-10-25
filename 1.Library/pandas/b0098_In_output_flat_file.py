import pandas as pd
from io import StringIO

data = """col1\tcol2\tcol3
1\t2\t3
4\t5\t6
7\t8\t9"""

df = pd.read_table(StringIO(data), sep='\t')
print("DataFrame from read_table:")
print(df)

data_csv = """col1,col2,col3
1,2,3
4,5,6
7,8,9"""

df_csv = pd.read_csv(StringIO(data_csv))
print("DataFrame from read_csv:")
print(df_csv)

csv_output = StringIO()
df_csv.to_csv(csv_output, index=False)
print("CSV format from DataFrame.to_csv():")
print(csv_output.getvalue())

data_fwf = """col1 col2 col3
1    2    3
4    5    6
7    8    9"""

df_fwf = pd.read_fwf(StringIO(data_fwf))
print("DataFrame from read_fwf:")
print(df_fwf)
