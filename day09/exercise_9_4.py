# Exercise 9-4: Number Served
# Build on your Restaurant class from Exercise 9-1.
# Add an attribute: number_served = 0 (default value in __init__)
# Add a method: set_number_served(number) — sets the count to a specific number
# Add a method: increment_number_served(amount) — adds to the count
#
# Create a 'restaurant' instance.
# Print number_served, change it, print again.
# Call set_number_served() and increment_number_served() and print results.

# TODO: Define Restaurant class with
# number_served attribute and two new methods
class Restaurant:
    """An attempt to create a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def description_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name.title()}")
        print(f"Cuisine Type: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, amount):
        self.number_served += amount


# TODO: Create an instance and demonstrate it
my_restaurant = Restaurant('fox hole', 'italian')
my_restaurant.description_restaurant()
my_restaurant.open_restaurant()
print(f"Number Served: {my_restaurant.number_served}")
my_restaurant.set_number_served(10)
print(f"Number Served: {my_restaurant.number_served}")
my_restaurant.increment_number_served(5)
print(f"Number Served: {my_restaurant.number_served}")
print("\n")

his_restaurant = Restaurant(
    restaurant_name='yard house',
    cuisine_type='american'
    )
his_restaurant.description_restaurant()
his_restaurant.open_restaurant()
print(f"Number Served: {his_restaurant.number_served}")
his_restaurant.set_number_served(20)
print(f"Number Served: {his_restaurant.number_served}")
his_restaurant.increment_number_served(10)
print(f"Number Served: {his_restaurant.number_served}")
print("\n")
