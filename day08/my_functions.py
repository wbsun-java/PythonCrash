# Exercise 8-16: Imports
# Take one of your earlier functions and store it in a separate module file.
# Then import it into this file using all five import styles:

def make_pizza(size, *toppings):
    """Summarize the pizza we're about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
