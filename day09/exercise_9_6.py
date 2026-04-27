# Exercise 9-6: Ice Cream Stand
# Write a class called IceCreamStand that inherits from Restaurant
# (Exercise 9-1 or 9-4).
# Add an attribute: flavors (a list of ice cream flavors)
# Add a method that displays the available flavors.
# Create an instance and call the method.

# TODO: Define Restaurant base class (or import from 9-1)
from restaurant import Restaurant


# TODO: Define IceCreamStand(Restaurant) with flavors list and display method
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print("Available Ice Cream Flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# TODO: Create an instance and call the display method
new_restaurant = Restaurant('fox hole', 'italian')
new_restaurant.description_restaurant()
new_restaurant.open_restaurant()
print("\n")

ice_cream_stand = IceCreamStand('yard', 'american')
ice_cream_stand.flavors = ['vanilla', 'chocolate', 'strawberry']
ice_cream_stand.display_flavors()
ice_cream_stand.description_restaurant()
ice_cream_stand.open_restaurant()
print("\n")
