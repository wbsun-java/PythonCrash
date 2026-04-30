# Exercise 10-2: Learning C
# Read each line from learning_python.txt.
# Use str.replace('Python', 'C') to substitute the language name.
# Print each modified line to the screen.

# TODO: Open learning_python.txt,
# read each line, replace 'Python' with 'C', print
with open('learning_python.txt') as file_object:
    for line in file_object:
        line = line.replace('Python', 'C')
        print(line.rstrip())
print()
