import unicodedata

# 특정 유니코드 문자의 이름 및 카테고리 조회
char = 'A'
name = unicodedata.name(char)
category = unicodedata.category(char)

print(f"Character: {char}")
print(f"Name: {name}")
print(f"Category: {category}")

# 결과:
# Character: A
# Name: LATIN CAPITAL LETTER A
# Category: Lu (Letter, Uppercase)

# 유니코드 문자 이름을 통해 문자 조회
name = "LATIN CAPITAL LETTER A"
char = unicodedata.lookup(name)

print(f"Name: {name}")
print(f"Character: {char}")

# 결과:
# Name: LATIN CAPITAL LETTER A
# Character: A


# 문자열의 각 문자에 대한 이름과 카테고리 조회
text = "Hello, World!"

for char in text:
    name = unicodedata.name(char, f"UNKNOWN ({char})")
    category = unicodedata.category(char)
    print(f"Character: {char}, Name: {name}, Category: {category}")

# 결과:
# Character: H, Name: LATIN CAPITAL LETTER H, Category: Lu
# Character: e, Name: LATIN SMALL LETTER E, Category: Ll
# Character: l, Name: LATIN SMALL LETTER L, Category: Ll
# Character: l, Name: LATIN SMALL LETTER L, Category: Ll
# Character: o, Name: LATIN SMALL LETTER O, Category: Ll
# Character: ,, Name: COMMA, Category: Po
# Character:  , Name: SPACE, Category: Zs
# Character: W, Name: LATIN CAPITAL LETTER W, Category: Lu
# Character: o, Name: LATIN SMALL LETTER O, Category: Ll
# Character: r, Name: LATIN SMALL LETTER R, Category: Ll
# Character: l, Name: LATIN SMALL LETTER L, Category: Ll
# Character: d, Name: LATIN SMALL LETTER D, Category: Ll
# Character: !, Name: EXCLAMATION MARK, Category: Po

# 정규화 예제
s1 = 'Café'
s2 = 'Cafe\u0301'  # Cafe + 음절 분리

print(f"Original: {s1}, {s2}")
print(f"Equal without normalization: {s1 == s2}")

# NFC (Normalization Form C) 정규화
s1_normalized = unicodedata.normalize('NFC', s1)
s2_normalized = unicodedata.normalize('NFC', s2)
print(f"Equal with NFC normalization: {s1_normalized == s2_normalized}")

# NFD (Normalization Form D) 정규화
s1_normalized = unicodedata.normalize('NFD', s1)
s2_normalized = unicodedata.normalize('NFD', s2)
print(f"Equal with NFD normalization: {s1_normalized == s2_normalized}")

# 결과:
# Original: Café, Café
# Equal without normalization: False
# Equal with NFC normalization: True
# Equal with NFD normalization: True

import unicodedata

# 유니코드 문자의 숫자 값 조회
chars = ['4', 'Ⅳ', 'ⅷ', '٢']

for char in chars:
    numeric_value = unicodedata.numeric(char, None)
    print(f"Character: {char}, Numeric value: {numeric_value}")

# 결과:
# Character: 4, Numeric value: 4.0
# Character: Ⅳ, Numeric value: 4.0
# Character: ⅷ, Numeric value: 8.0
# Character: ٢, Numeric value: 2.0