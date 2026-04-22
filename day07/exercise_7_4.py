# Exercise 7-4: Pizza Toppings
# Write a loop that prompts for pizza toppings until the user enters 'quit'.
# For each topping entered, print: "I'll add [topping] to your pizza."

# TODO: Write a while loop that collects toppings
while True:
    toppings = input("Enter a pizza topping (or 'quit' to finish): ")
# TODO: Break out of the loop when user types 'quit'
    if toppings == 'quit':
        break
# TODO: Print a confirmation message for each topping
    else:
        print(f"I'll add {toppings} to your pizza.")
print("Thank you for your order!")
