# Compare integers
number = 10
if number > 5:
    print("number is greater than 5.")

# Comparing decimals
pi = 3.14
if pi == 3.14:
    print("pi is 3.14.")

# Compare strings
name = "Alice"
if name == "Alice":
    print("Hello, Alice!")

# Check if a string is included
sentence = "Python is a powerful language."
if "Python" in sentence:
    print("Found Python in the sentence.")

#Check if a value exists in the list
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("There's apple in the list.")

# Using the length of a list as a condition
if len(fruits) > 2:
    print("There are more than 3 fruits in the list.")

# Check if a key exists in the dictionary
person = {"name": "Bob", "age": 25}
if "name" in person:
    print("The name key exists.")

# Checking for specific value conditions
if person.get("age") and person["age"] > 20:
    print("Age is 20 or older.")

# Determine if an element exists in a set
unique_numbers = {1, 2, 3, 4, 5}
if 3 in unique_numbers:
    print("The set contains 3.")

# Determine whether a set is a union
another_set = set()
if not another_set:
    print("The set is empty.")

# Verify tuple values
coordinates = (10, 20)
if len(coordinates) == 2:
    print("Coordinates are two-dimensional.")

# Verify a specific value
if 10 in coordinates:
    print("Tuple contains 10.")

# Verify boolean values
is_active = True
if is_active:
    print("Active status.")

# Using the negation operator
if not is_active:
    print("Disabled.")

# Confirm None
value = None
if value is None:
    print("No value.")

#If not None
value = 10
if value is not None:
    print("The value exists :", value)

age = 30
city = "New York"

if age > 20 and city == "New York":
    print("I'm over 20 years old and live in New York City.")

if age < 18 or city == "New York":
    print("I'm a minor or live in New York.")

data = [1, 2, 3]

if isinstance(data, list):
    print("data is a list.")

value = 42
if isinstance(value, int):
    print("value is an integer.")