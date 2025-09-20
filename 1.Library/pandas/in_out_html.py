import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
tables = pd.read_html(url)
df = tables[0]
print("First table from the HTML page:")
print(df.head())

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
})
html_data = df.to_html()
print("DataFrame as HTML:")
print(html_data)
df.to_html('output_table.html')

html_data_with_style = df.to_html(classes='table table-striped', border=2)
print("DataFrame with HTML style:")
print(html_data_with_style)
df.to_html('styled_output_table.html', classes='table table-striped', border=2)
