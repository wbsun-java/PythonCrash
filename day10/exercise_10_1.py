# Exercise 10-1: Learning Python
# First, create a file called learning_python.txt in this directory.
# Write a few lines in it, each starting with "In Python you can..."
#
# Then write a program that reads the file and prints it THREE ways:
# 1. Read the entire file at once (read())
# 2. Loop over the file object line by line
# 3. Read lines into a list (readlines()),
#    then print from the list outside the with block

# TODO: Create learning_python.txt with several "In Python you can..." lines
# TODO: Method 1 — read entire file with read()
with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)
print()
# TODO: Method 2 — loop over file object inside with block
with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
print()
# TODO: Method 3 — use readlines() and print from list outside the with block
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
print()
