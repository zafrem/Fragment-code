# 1. create a list
empty_list = []
fruits = ["apple", "banana", "cherry"]
print("Created list:", fruits)

# 2. copy the list
fruits_copy = fruits.copy()
fruits_copy_slice = fruits[:]
fruits_copy[0] = "grape"
print("Original list:", fruits)
print("Copied list (copy method):", fruits_copy)
print("Copied list (slicing):", fruits_copy_slice)

# 3. Delete the list
del fruits[1] # Delete 'banana' at index 1
print("List after deleting 'banana':", fruits)
fruits.remove("cherry") # remove 'cherry'
print("List after deleting ‘cherry’:", fruits)

# 4. add a list item
fruits = ["apple"]
fruits.append("banana")
print("List after adding 'banana':", fruits)
fruits.insert(1, "cherry")
print("List after adding ‘cherry’:", fruits)
fruits.extend(["grape", "orange"])
print("‘grape’, ‘orange’ added to list:", fruits)

# 5. Delete a list item
popped_item = fruits.pop(2)
print("Item deleted with 'pop' method:", popped_item)
print("List after deleting ‘cherry’:", fruits)
fruits.remove("apple")
print("‘apple’ deleted and listed:", fruits)
fruits.clear()
print("List after removing all items:", fruits)

# 6. Change list items
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)
fruits[1] = "grape"
print("List after replacing ‘banana’ with ‘grape’:", fruits)