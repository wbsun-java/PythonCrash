# Chapter 10 — Files and Exceptions
# Key examples from the book

# To run the file examples, first create pi_digits.txt with some text.

# --- Reading an entire file ---
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)

# --- Reading line by line ---
# with open('pi_digits.txt') as file_object:
#     for line in file_object:
#         print(line.rstrip())   # rstrip removes the extra newline

# --- Storing lines in a list ---
# with open('pi_digits.txt') as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.rstrip())

# --- Writing to a file ---
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# --- Appending to a file ---
with open(filename, 'a') as file_object:
    file_object.write("I also love working with data.\n")

# --- Reading back what we wrote ---
with open(filename) as file_object:
    print(file_object.read())

# --- try-except: ZeroDivisionError ---
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# --- try-except-else ---
print("Give me two numbers, and I'll divide them.")
# first_number = input("First number: ")
# second_number = input("Second number: ")
first_number = '10'
second_number = '2'
try:
    answer = int(first_number) / int(second_number)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(answer)

# --- FileNotFoundError ---
filename = 'nonexistent_file.txt'
try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

# --- Silent failure with pass ---
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass   # silently ignore missing files

# --- Storing data with json ---
import json

# Write
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

# Read back
with open(filename) as f:
    numbers = json.load(f)
print(numbers)

# --- Remembering a user (json pattern) ---
import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

# greet_user()   # uncomment to run interactively
