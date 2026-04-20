# Exercise 4-11: My Pizzas, Your Pizzas
# Start with your program from Exercise 4-1.
# Make a copy of the list of pizzas, and call it friend_pizzas.
# Add a new pizza to the original list.
# Add a different pizza to friend_pizzas.
# Prove that you have two separate lists by printing "My favorite pizzas are:"
# then your list, and "My friend's favorite pizzas are:" then friend_pizzas.

my_pizzas = ['margherita', 'pepperoni', 'bbq chicken']
friend_pizzas = my_pizzas[:]  # copy using slice

my_pizzas.append('hawaiian')
friend_pizzas.append('veggie')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"  {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"  {pizza}")

my_items = ['iphone', 'ipad', 'mac']
friend_items = my_items[:]

my_items.append('watch')
friend_items.append('tv')

for item in my_items:
    print(f"My {item}")

for item in friend_items:
    print(f"My friend's {item}")
