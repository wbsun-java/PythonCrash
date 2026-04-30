# Exercise 10-8: Cats and Dogs
# Create two files: cats.txt and dogs.txt (at least 3 names each).
# Write a program that reads and prints both files.
# Wrap in a try-except to catch FileNotFoundError with a friendly message.
# Then MOVE one file to test the except block fires.

# TODO: Create cats.txt and dogs.txt with animal names

# TODO: Try to read and print both files
try:
    with open('cats.txt') as file_object:
        cats = file_object.read()
        print(cats)
    with open('dogs.txt') as file_object:
        dogs = file_object.read()
        print(dogs)

# TODO: Catch FileNotFoundError and print a friendly message
except FileNotFoundError:
    print("One or both files don't exist.")
