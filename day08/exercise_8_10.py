# Exercise 8-10: Great Magicians
# Build on Exercise 8-9.
# Write a function called make_great() that modifies the magicians list
# by adding "the Great" to each name (e.g., "the Great Alice").
# Call show_magicians() after to verify the list was modified.

magicians = ['alice', 'david copperfield', 'criss angel', 'penn']


# TODO: Define make_great(magicians) that modifies the list in-place
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = 'the Great ' + magicians[i]


# TODO: Define show_magicians(magicians) that prints each name
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


# TODO: Call make_great() then show_magicians() to confirm the change
make_great(magicians)
show_magicians(magicians)
