# Exercise 10-11: Favorite Number
# Prompt for the user's favorite number.
# Use json.dump() to store the number in a file called favorite_number.json.

import json

# TODO: Prompt for favorite number
num = int(input("What is your favorite number? "))
# TODO: Use json.dump() to save it to favorite_number.json
print(f"I'll remember that {num} is your favorite number!")
with open('favorite_number.json', 'w') as f:
    json.dump(num, f)
print()
