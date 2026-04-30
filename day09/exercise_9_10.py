# Exercise 9-10: Imported Restaurant
# Store your Restaurant class in a module called restaurant.py
# In this file, import Restaurant from that module.
# Create a Restaurant instance and 
# call one of its methods to verify the import works.

import restaurant


# TODO: Create restaurant.py with the Restaurant class
# TODO: In this file: from restaurant import Restaurant

# TODO: Create an instance and call a method
my_favorite_restaurant = restaurant.Restaurant(
    'home',
    'anything my wife cooks'
)
my_favorite_restaurant.description_restaurant()
my_favorite_restaurant.open_restaurant()
print("\n")

my_2nd_favorite_restaurant = restaurant.Restaurant(
    'yard house',
    'american'
)
my_2nd_favorite_restaurant.description_restaurant()
my_2nd_favorite_restaurant.open_restaurant()
print("\n")
