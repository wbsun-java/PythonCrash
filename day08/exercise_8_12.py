# Exercise 8-12: Sandwiches
# Write a function that accepts an arbitrary number of sandwich items (*args).
# Print a summary of the sandwich being ordered.
# Call the function three times with different numbers of items.

# TODO: Define a function with *toppings (or *items) parameter
def make_sandwich(*toppings):
    for topping in toppings:
        print(f"Adding {topping} to your sandwich.")


# TODO: Call it three times with different numbers of arguments
make_sandwich('pepperoni', 'cheese', 'lettuce', 'tomato')
make_sandwich('turkey', 'avocado')
make_sandwich('peanut butter')
