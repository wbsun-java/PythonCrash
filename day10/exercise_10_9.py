# Exercise 10-9: Silent Cats and Dogs
# Modify Exercise 10-8 so the except block fails SILENTLY.
# Use 'pass' in the except block — no message printed if a file is missing.

# TODO: Same as 10-8 but use 'pass' in the except block (silent failure)
try:
    with open('cats.txt') as file_object:
        cats = file_object.read()
        print(cats)
    with open('dogs.txt') as file_object:
        dogs = file_object.read()
        print(dogs)

except FileNotFoundError:
    pass
print()
