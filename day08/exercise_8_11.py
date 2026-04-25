# Exercise 8-11: Unchanged Magicians
# Build on Exercise 8-10.
# Call make_great() with a COPY of the magicians list.
# Return the new list from make_great() and store it in a separate variable.
# Call show_magicians() with both lists:
#   - the original (should be unchanged)
#   - the new list (should have "the Great" added)

magicians = ['alice', 'david copperfield', 'criss angel', 'penn']


# TODO: Define make_great(magicians) that
# returns a NEW list (does not modify original)
def make_magicians(magicians):
    new_magicians = []
    for magician in magicians:
        new_magicians.append(magician)
    return new_magicians


# TODO: Define show_magicians(magicians) that prints each name
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


# TODO: Call make_great() with a copy (magicians[:]), store in great_magicians
great_magicians = make_magicians(magicians[:])


def make_great(great_magicians):
    for i in range(len(great_magicians)):
        great_magicians[i] = 'the Great ' + great_magicians[i]


make_great(great_magicians)


# TODO: Call show_magicians() on both original and great_magicians
show_magicians(magicians)
show_magicians(great_magicians)
