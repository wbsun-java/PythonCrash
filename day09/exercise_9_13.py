# Exercise 9-13: OrderedDict Rewrite
# Take your glossary from Exercise 6-4 and rewrite it using OrderedDict.
# The order of the output should match the order you added the key-value pairs.
# from collections import OrderedDict

from collections import OrderedDict


# TODO: Create an OrderedDict called glossary with 5+ programming terms
glossary = OrderedDict()
glossary['variables'] = 'A variable is a name that refers to a value.'
glossary['lists'] = 'A list is an ordered sequence of items.'
glossary['dictionaries'] = ('A dictionary is an unordered collection of '
                            'key-value pairs.')
glossary['tuples'] = 'A tuple is an immutable ordered sequence of items.'
glossary['sets'] = 'A set is an unordered collection of unique items.'
glossary['functions'] = ('A function is a block of code that performs a '
                         'specific task.')
glossary['classes'] = 'A class is a blueprint for creating objects.'
glossary['objects'] = 'An object is an instance of a class.'
glossary['methods'] = 'A method is a function that belongs to a class.'
glossary['attributes'] = 'An attribute is a variable that belongs to a class.'


for word, definition in glossary.items():
    print(f"{word.title()}: {definition}\n")
