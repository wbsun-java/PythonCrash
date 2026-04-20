# Exercise 6-3: Glossary
# Create a glossary of 5 programming terms you've learned.
# - Keys = the programming words
# - Values = their meanings
# Print each word and its meaning neatly.
# Use \n to insert a blank line between each word-meaning pair.

# TODO: Create a glossary dictionary with 5 programming terms and definitions
# TODO: Print each word followed by its meaning
# (use \n for blank lines between pairs)
glossary = {
    'variables': 'A variable is a name that refers to a value.',
    'lists': 'A list is an ordered sequence of items.',
    'dictionaries': ('A dictionary is an unordered collection of '
                     'key-value pairs.'),
    'tuples': 'A tuple is an immutable ordered sequence of items.',
    'sets': 'A set is an unordered collection of unique items.',
}
for word, definition in glossary.items():
    print(f"{word.title()}: {definition}\n")
