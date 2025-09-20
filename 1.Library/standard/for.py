
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

for i in range(5):
    print(i)

numbers = [1, 2, 3, 4, 5]
squared_numbers = [num * 2 for num in numbers]
print(squared_numbers)

for i in range(1, 10, 2):
    print(i)

person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key, value in person.items():
    print(f"{key}: {value}")

word = "Python"
for char in word:
    print(char)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element)

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        print(num)

numbers = [1, 2, 3, 4, 5]

print("Using break:")
for num in numbers:
    if num == 3:
        break
    print(num)

print("\nUsing continue:")
for num in numbers:
    if num == 3:
        continue
    print(num)

for num in range(5):
    print(num)
else:
    print("The iteration is finished.")

unique_numbers = {1, 2, 3, 4, 5}
for num in unique_numbers:
    print(num)
