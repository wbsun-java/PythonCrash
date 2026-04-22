# Exercise 7-10: Dream Vacation
# Poll users about their dream vacation.
# Prompt: "If you could visit one place in the world, where would you go?"
# Keep asking until user enters 'quit'.
# Store each response in a dictionary: {name: place}
# After polling, print all the results.

responses = {}

# TODO: Write a while loop that asks for name and dream vacation
while True:
    name = input("What is your name? ")
    if name == 'quit':
        break
    place = input("If you could visit one place in the world, "
                  "where would you go? ")
    # TODO: Store each response in the 'responses' dictionary
    responses[name] = place
# TODO: After loop ends, print all names and their dream destinations
for name, destinations in responses.items():
    print(f"{name.title()}'s dream destinations: {destinations.title()}")
