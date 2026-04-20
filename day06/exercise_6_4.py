# Exercise 6-4: Glossary 2
# Improve your Exercise 6-3 code by using a loop 
# instead of separate print statements.
# Add 5 more programming terms to the glossary (10 total).
# The loop should automatically print all of them.

# TODO: Create glossary dict with at least 10 programming terms
# TODO: Use a for loop to print each word and its meaning
glossary = {
    'variables': 'A variable is a name that refers to a value.',
    'lists': 'A list is an ordered sequence of items.',
    'dictionaries': ('A dictionary is an unordered collection of '
                     'key-value pairs.'),
    'tuples': 'A tuple is an immutable ordered sequence of items.',
    'sets': 'A set is an unordered collection of unique items.',
    'functions': ('A function is a block of code that performs a '
                  'specific task.'),
    'classes': 'A class is a blueprint for creating objects.',
    'objects': 'An object is an instance of a class.',
    'methods': 'A method is a function that belongs to a class.',
    'attributes': 'An attribute is a variable that belongs to a class.',
}

for word, definition in glossary.items():
    print(f"{word.title()}: {definition}\n")
