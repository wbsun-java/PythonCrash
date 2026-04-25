# Exercise 8-9: Magicians
# Make a list of magician names.
# Pass the list to a function called show_magicians() that prints each name.

magicians = ['alice', 'david copperfield', 'criss angel', 'penn']


# TODO: Define show_magicians(magicians) that prints each name
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


# TODO: Call show_magicians() with your list
show_magicians(magicians)
