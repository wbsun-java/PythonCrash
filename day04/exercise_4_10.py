# Exercise 4-10: Slices
# Using one of the programs you wrote in this chapter, add several lines to the end
# that do the following:
# - Print "The first three items in the list are:" then use a slice to print those items.
# - Print "Three items from the middle of the list are:" then use a slice.
# - Print "The last three items in the list are:" then use a slice.

places = ['Paris', 'Tokyo', 'New York', 'Sydney', 'Rome', 'London', 'Berlin']

print("The first three items in the list are:")
print(places[:3])

# TODO: Print the middle three items using a slice
print(f"There are three items in the middle of the list: {places[2:5]}")

# TODO: Print the last three items using a slice
print(f"These are the last three items in the list: {places[-3:]}.")

print(f"These are the items of the list: {places[:]}.")

print(f"Print again {places[1:-1]}.")

print(f"Again: {places[0:6]}")