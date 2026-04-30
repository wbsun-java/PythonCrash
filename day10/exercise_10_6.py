# Exercise 10-6: Addition
# Prompt for two numbers, add them, and print the result.
# Use a try-except block to catch ValueError if 
# the user enters text instead of a number.
# Print a friendly error message if the input isn't a number.

# TODO: Prompt for two numbers
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
# TODO: Try to convert to int/float and add them
try:
    num1 = float(num1)
    num2 = float(num2)
    print(f"{num1} + {num2} = {num1 + num2}")
    print()
# TODO: Catch ValueError and print a friendly message
except ValueError:
    print("Your input isn't a number.")
print()
