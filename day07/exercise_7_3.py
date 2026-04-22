# Exercise 7-3: Multiples of Ten
# Ask the user for a number.
# Report whether the number is a multiple of 10 or not.
# Hint: use the modulo operator %

# TODO: Use input() to get a number (convert to int)
number = input("Enter a number: ")
number = int(number)
# TODO: Check if it's a multiple of 10 using %
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
