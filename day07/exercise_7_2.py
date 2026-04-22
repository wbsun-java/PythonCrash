# Exercise 7-2: Restaurant Seating
# Ask the user how many people are in their dinner group.
# - More than 8: "You'll have to wait for a table."
# - 8 or fewer: "Your table is ready."

# TODO: Use input() to get the number of people (convert to int)
guests = input("How many people are in your dinner group? ")
guests = int(guests)
# TODO: Use an if/else to print the appropriate message
if guests > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")
