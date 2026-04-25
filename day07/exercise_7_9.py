# Exercise 7-9: No Pastrami
# Start from Exercise 7-8.
# Make sure 'pastrami' appears at least 3 times in sandwich_orders.
# Print a message that the deli has run out of pastrami.
# Use a while loop to remove ALL occurrences of 'pastrami' from the list.
# Then make the remaining sandwiches and move them to finished_sandwiches.
# Make sure no pastrami ends up in finished_sandwiches.

sandwich_orders = ['pastrami',
                   'tuna',
                   'pastrami',
                   'egg salad',
                   'pastrami',
                   'blt']
finished_sandwiches = []

# TODO: Print "We're out of pastrami!".
print("We're out of pastrami!")
# TODO: Use a while loop to remove all 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
# TODO: Then process the remaining orders (like exercise 7-8)
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
print(f"Finished sandwiches: {finished_sandwiches}")
