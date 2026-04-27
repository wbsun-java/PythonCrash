# Exercise 9-1: Restaurant
# Create a class called Restaurant with:
# - __init__: stores restaurant_name and cuisine_type
# - describe_restaurant(): prints the name and cuisine type
# - open_restaurant(): prints a message that the restaurant is open
#
# Create an instance called 'restaurant'.
# Print the two attributes individually, then call both methods.

# TODO: Define the Restaurant class
class Restaurant:
    """An attempt to create a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def description_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name.title()}")
        print(f"Cuisine Type: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")


# TODO: Create an instance and demonstrate it
my_restaurant = Restaurant('fox hole', 'italian')
my_restaurant.description_restaurant()
my_restaurant.open_restaurant()
