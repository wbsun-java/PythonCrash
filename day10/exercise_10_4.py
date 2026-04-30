# Exercise 10-4: Guest Book
# Write a while loop that repeatedly asks users for their name.
# Each time: print a greeting to the screen
# AND append their name to guest_book.txt.
# Make sure each entry is on a new line in the file.
# Exit when user types 'quit'.

# TODO: While loop asking for name
while True:
    name = input("What is your name? ")
    if name == 'quit':
        break

# TODO: Print greeting to screen
    print(f"Hello, {name.title()}!")
# TODO: Append name to guest_book.txt with a newline
    with open('guest_book.txt', 'a') as file_object:
        file_object.write(f"{name}\n")
print()
