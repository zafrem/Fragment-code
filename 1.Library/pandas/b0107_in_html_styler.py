import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 95, 78],
    'Science': [88, 90, 92],
    'English': [91, 89, 85]
})

styled_df = df.style.highlight_max(color='lightgreen', axis=0)\
    .highlight_min(color='lightcoral', axis=0)\
    .set_caption("Student Grades")

html_output = styled_df.to_html()
print("Styled DataFrame as HTML:")
print(html_output)

with open('styled_dataframe.html', 'w') as file:
    file.write(html_output)
print("Styled DataFrame saved as 'styled_dataframe.html'")
