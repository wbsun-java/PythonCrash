# Exercise 8-15: Printing Models
# The book shows a print_models.py example with two functions:
#   - print_models(unprinted, completed)
#   - show_completed_models(completed)
#
# This exercise: put those functions in a separate file called
# printing_functions.py
# Then import and use them here in exercise_8_15.py.
#
# Step 1: Create printing_functions.py with both functions
# Step 2: In this file, add: from printing_functions import print_models,
# show_completed_models
# Step 3: Call them here


# TODO: Create printing_functions.py with the two functions

# TODO: Import and use them below
from printing_functions import print_models, show_completed_models

unprinted = ['phone case', 'robot pendant', 'dodecahedron']
completed = []

print_models(unprinted, completed)
show_completed_models(completed)
