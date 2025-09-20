# Example of outputting 1 through 10
counter = 1
while counter <= 10:
    print(counter)
    counter += 1

# Keep asking until the user types 'exit'
user_input = ""
while user_input != "exit":
    user_input = input("To exit, type 'exit': ")
    print(f"The value input: {user_input}")

# Increment infinitely from 1 and end at 5
num = 1
while True:
    print(num)
    if num == 5:
        print("Reached 5. Exit.")
        break
    num += 1

# Print up to 10 but skip 5, exit after 8
num = 1
while num <= 10:
    if num == 5:
        num += 1
        continue  # Skip step 5
    elif num > 8:
        print("Over 8. Exit.")
        break  # exit if num > 8
    print(num)
    num += 1


import random

# Example of exiting if the random number is 3
while True:
    rand_num = random.randint(1, 5)  # Generate random integers from 1 to 5
    print(f"Generated numbers: {rand_num}")
    if rand_num == 3:
        print("3 has been created. Exit.")
        break

# A while statement that traverses all elements of a list
items = ["apple", "banana", "cherry"]
index = 0

while index < len(items):
    print(items[index])
    index += 1

import time

# Repeat for 5 seconds
start_time = time.time()
while True:
    current_time = time.time()
    if current_time - start_time > 5:  # If 5 seconds have passed, exit
        print("5 seconds have passed. Exit.")
        break
    print("Repeating...")
    time.sleep(1)  # Wait 1 second

# Exit with flag variables
keep_running = True
count = 0

while keep_running:
    print("Repeating...")
    count += 1
    if count >= 3:
        keep_running = False
        print("End the loop.")