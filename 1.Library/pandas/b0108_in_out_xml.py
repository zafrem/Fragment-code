import pandas as pd
from io import StringIO

xml_data = '''<?xml version="1.0" encoding="UTF-8" ?>
<data>
    <row>
        <Name>Alice</Name>
        <Age>25</Age>
        <City>New York</City>
    </row>
    <row>
        <Name>Bob</Name>
        <Age>30</Age>
        <City>San Francisco</City>
    </row>
    <row>
        <Name>Charlie</Name>
        <Age>35</Age>
        <City>Los Angeles</City>
    </row>
</data>
'''
df = pd.read_xml(StringIO(xml_data))
print("DataFrame from XML:")
print(df)

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
})
xml_output = df.to_xml()
print("DataFrame to XML:")
print(xml_output)

df.to_xml('output_data.xml')
print("DataFrame saved as 'output_data.xml'")
