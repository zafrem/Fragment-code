my_dict = {
    "name": "CIL",
    "age": 1,
    "site": "Blogger"
}
print(my_dict["name"]) # output : CIL
print(my_dict["age"]) # output : 1

# Add Value
my_dict["email"] = "cil@blogger.com"

# Edit Value
my_dict["age"] = 2

# delete Key:value
del my_dict["site"]

print(my_dict) # output : {'name': 'CIL', 'age': 2, 'email': 'cil@blogger.com'}

for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(f"{key}: {value}")

keys = my_dict.keys()
print(keys) # output : dict_keys(['name', 'age', 'email'])

values = my_dict.values()
print(values) # output : dict_values(['CIL', 2, 'cil@blogger.com'])

items = my_dict.items()
print(items)
# output : dict_items([('name', 'CIL'), ('age', 2), ('email', 'cil@blogger.com')])

if "name" in my_dict:
    print("Name in dictionary")

major = my_dict.get("major", "Undeclared")
print(major) # output : Undeclared

# default key
graduation_year = my_dict.setdefault("graduation_year", 2024)
print(graduation_year)  # output : 2024
print(my_dict)
# output : {'name': 'CIL', 'age': 2, 'email': 'cil@blogger.com',
# 'graduation_year': 2024}
