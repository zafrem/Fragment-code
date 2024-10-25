import pandas as pd

# pip install jinja2

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 92, 78],
    'Grade': ['B', 'A', 'C']
})

styled_df = df.style.map(lambda x: 'background-color: yellow' if isinstance(x, int) and x < 80 else '')
styled_df.to_excel('styled_output.xlsx', engine='openpyxl', index=False)

# Conditional
styled_df = df.style.map(lambda x: 'background-color: yellow' if isinstance(x, str) else '') \
                    .map(lambda x: f'color: {"green" if x >= 80 else "red"}' if isinstance(x, int) else '')
styled_df.to_excel('styled_output_conditional.xlsx', engine='openpyxl', index=False)

# Mutiple
styled_df = df.style \
    .map(lambda x: 'background-color: lightblue' if isinstance(x, str) else '') \
    .highlight_max(subset=['Score'], color='lightgreen') \
    .highlight_min(subset=['Score'], color='lightcoral')
styled_df.to_excel('styled_output_multiple_styles.xlsx', engine='openpyxl', index=False)

# Formatting
styled_df = df.style.format({'Score': '{:.2f}'}) \
                    .map(lambda x: 'background-color: #FFC7CE' if isinstance(x, int) and x < 80 else '')
styled_df.to_excel('styled_output_formatting.xlsx', engine='openpyxl', index=False)

