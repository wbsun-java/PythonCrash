# Exercise 4-13: Buffet
# A buffet-style restaurant offers only five basic foods.
# Store them in a tuple.
# Use a for loop to print each food the restaurant offers.
# Try to modify one of the items — notice the error.
# The restaurant changes its menu, replacing two of the items.
# You can't modify a tuple, but you can assign a new tuple to the same variable.
# Make the change and use a for loop to print each item from the revised menu.

# TODO: Define a tuple of 5 foods, loop through it,
#       then reassign the variable to a new tuple with two items changed
menu = ('steak', 'rice', 'noodle', 'pizza', 'pasta')
print("My restaurant offers the following foods:")
for food in menu:
    print(f" {food}.")

# menu[1] = 'sushi' #tuple object does not support item assignment

menu = ('sushi', 'rice', 'noodle', 'pizza', 'pasta')
print("Updated menu:")
for food in menu:
    print(f" {food}.")
