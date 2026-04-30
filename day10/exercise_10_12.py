# Exercise 10-12: Favorite Number Remembered
# Combine Exercises 10-11 and a reader into one program:
# - If favorite_number.json exists, load it and print:
# "I know your favorite number! It's ___."
# - If not, prompt for the number and save it.
# Run twice to see both paths.

import json

# TODO: Try to load favorite_number.json
try:
    with open('favorite_number.json') as f:
        num = json.load(f)
# TODO: If found, print the remembered number
    print(f"I know your favorite number! It's {num}.")
# TODO: If FileNotFoundError, prompt for a number and save it with json.dump() 
except FileNotFoundError:
    num = int(input("What is your favorite number? "))
    with open('favorite_number.json', 'w') as f:
        json.dump(num, f)
    print(f"I'll remember that {num} is your favorite number!")
print()
