colors = ['red', 'blue', 'black']

colors.append('white')
print(colors)  # ['red', 'blue', 'black', 'white']

# insert list
colors.insert(1, 'yellow')
print(colors)  # ['red', 'yellow', 'blue', 'black', 'white']

# edit list
colors[2] = 'gray'
print(colors)  # ['red', 'yellow', 'gray', 'black', 'white']

# delete list
colors.remove('yellow')
print(colors)  # ['red', 'gray', 'black', 'white']

# size of list
print(len(colors))  # 4

for color in colors:
    print(color)

# slice
print(colors[1:3])  # ['gray', 'black']

print(type(colors))
colors = tuple(colors)
print(type(colors))

print(colors[0])  # 'red'
print(colors[1:3])  # ('gray', 'black')

# size of tuple
print(len(colors))  # 4

for color in colors:
    print(color)

colors_list = list(colors)
print(colors_list)  # ['red', 'gray', 'black', 'white']
