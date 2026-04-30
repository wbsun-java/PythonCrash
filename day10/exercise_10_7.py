# Exercise 10-7: Addition Calculator
# Wrap your Exercise 10-6 code in a while loop
# so users can keep entering numbers.
# If they enter text, show the friendly error and keep going.
# Exit when user types 'quit'.

# TODO: While loop wrapping the addition code from 10-6
while True:
    num1 = input("Enter a number: (or 'quit' to exit)")
    if num1 == 'quit':
        break
    num2 = input("Enter another number: (or 'quit' to exit)")
    if num2 == 'quit':
        break
# TODO: Try to convert to int/float and add them
    try:
        num1 = float(num1)
        num2 = float(num2)
        print(f"{num1} + {num2} = {num1 + num2}")
        print()

# TODO: Handle ValueError gracefully and continue the loop
    except ValueError:
        print("Your input isn't a number.")
        print()
# TODO: Exit on 'quit'