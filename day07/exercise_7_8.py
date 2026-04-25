# Exercise 7-8: Deli
# Make a list called sandwich_orders with sandwich names.
# Make an empty list called finished_sandwiches.
# Loop through sandwich_orders:
#   - Print "I made your [sandwich] sandwich."
#   - Move each sandwich from sandwich_orders to finished_sandwiches.
# After all sandwiches are made, print a summary of what was made.

sandwich_orders = ['tuna', 'pastrami', 'egg salad', 'blt', 'veggie']
finished_sandwiches = []

# TODO: Loop through sandwich_orders using a while loop
while sandwich_orders:
    # TODO: Print a message for each sandwich and
    # move it to finished_sandwiches
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    # TODO: Print a summary list of all finished sandwiches
    finished_sandwiches.append(sandwich)
print(f"Finished sandwiches: {finished_sandwiches}")
