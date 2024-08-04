import re

# Matching
pattern = r'[34569]\d{3}-\d{4}-\d{4}-\d{4}'
text = "My card number is 9923-2341-2354-2385."

match = re.search(pattern, text)
if match:
    print("Match found:", match.group())  # Match found: 9923-2341-2354-2385
else:
    print("No match found")

pattern = r'\d+'  # Chase only numbers

matches = re.findall(pattern, text)
print("Matches found:", matches)  # Matches found: ['9923', '2341', '2354', '2385']

# replace (this is masking)
new_text = re.sub(pattern, '****', text)
print("Replaced text:", new_text)
    # Replaced text: My card number is ****-****-****-****.

# group
print(re.match('(23)', text)) # None - First
print(re.search('(23)', text)) # <re.Match object; span=(20, 22), match='23'>
print(re.findall('(23)', text)) # ['23', '23', '23', '23']
print(re.fullmatch('(23)', text)) # None

# capture
pattern = '(\d\d\d\d)'
match = re.findall(pattern, text)
if match:
    print(f"{match[0]}-{match[1]}-{match[2]}-{match[3]}") #
else:
    print("No match found")

# compile
pattern = re.compile(r'\b\w{2}\b')  # 2-letter
matches = pattern.findall(text)
print("2-letter words:", matches)  # ['My', 'is']

# Start pattern
pattern_start = r'^My'

if re.match(pattern_start, text):
    print("The string starts with 'My'")  # The string starts with 'My'
else:
    print("The string does not start with 'My'")

# End pattern
pattern_end = r'.$'

if re.search(pattern_end, text):
    print("The string ends with '.'")  # The string ends with '.'
else:
    print("The string does not end with '.'")

# Multiple lines
pattern = r'^\w+'  # Fist word
text = """first line
        second line
third line"""
matches = re.findall(pattern, text, re.MULTILINE)
print("Words at the start of each line:", matches)  # ['first', 'third']

# 비어 있지 않은 줄 찾기
pattern = r'^.+$'
text = """first line
    second line

third line
"""
matches = re.findall(pattern, text, re.MULTILINE)
print("Non-empty lines:", matches) # ['first line', '    second line', 'third line']