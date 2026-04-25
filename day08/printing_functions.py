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

def print_models(unprinted, completed):
    """Print the models and show completed models"""
    while unprinted:
        current = unprinted.pop()
        print(f"Printing model: {current}")
        completed.append(current)


def show_completed_models(completed):
    """Show the completed models"""
    print("\nCompleted:", completed)
