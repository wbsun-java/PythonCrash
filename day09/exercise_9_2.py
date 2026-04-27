# Exercise 9-2: Three Restaurants
# Use your Restaurant class from Exercise 9-1.
# Create 3 different instances, each with different name and cuisine type.
# Call describe_restaurant() for each instance.

# TODO: Copy or import your Restaurant class from 9-1
# TODO: Create 3 instances and call describe_restaurant() on each
from restaurant import Restaurant


my_restaurant = Restaurant('fox hole', 'italian')
my_restaurant.description_restaurant()
my_restaurant.open_restaurant()

his_restaurant = Restaurant(restaurant_name='yard house', cuisine_type='american')
his_restaurant.description_restaurant()
his_restaurant.open_restaurant()
