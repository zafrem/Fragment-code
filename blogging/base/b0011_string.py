first = "A"
second = "B"
full = first + " " + second
print(full)  # "A B"

repeat_str = "Ha " * 3
print(repeat_str)  # "Ha Ha Ha"

# size of
_str = ' Hi my name is John '
length = len(_str)
print(length)  # 20

# indexing
print(_str[1])  # "H"
print(_str[-2])  # "n"

# slice
print(_str[7:12])  # "name"
print(_str[:5])  # " Hi m"
print(_str[7:])  # "name is John "

# Capital
print(_str.upper())  # " HI MY NAME IS JOHN "
print(_str.lower())  # " hi my name is john "
print(_str.capitalize())  # " hi my name is john "
print(_str.title())  # " Hi My Name Is John "

print(_str.strip())  # "Hi my name is John"
print(_str.lstrip())  # "Hi my name is John "
print(_str.rstrip())  # " Hi my name is John"

# find, replace
print(_str.find("John"))  # 15
print(_str.find("World"))  # -1
print(_str.replace("John", "Jang"))  # " Hi my name is Jang "

# f-strings (Python 3.6+)
name = "John"
age = 1
intro = f"Hi~ My name is {name}, I am {age} years old."
print(intro)  # "MHi~ My name is John, I am 1 years old."

# str.format()
intro_format = "Hi~ My name is {}, I am {} years old.".format(name, age)
print(intro_format)  # "Hi~ My name is John, I am 1 years old."

# %
intro_percent = "Hi~ My name is %s, I am %d years old." % (name, age)
print(intro_percent)  # "Hi~ My name is John, I am 1 years old."

# Split
sentence = "This is a sentence."
words = sentence.split()
print(words)  # ['This', 'is', 'a', 'sentence.']

# join
joined_sentence = ' '.join(words)
print(joined_sentence)  # "This is a sentence."