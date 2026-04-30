# Exercise 10-3: Guest
# Prompt the user for their name.
# Write their name to a file called guest.txt.

# TODO: Use input() to get the user's name
name = input("What is your name? ")
# TODO: Write the name to guest.txt using open(..., 'w')
with open('guest.txt', 'w') as file_object:
    file_object.write(name)
print(f"Hello, {name.title()}!")
