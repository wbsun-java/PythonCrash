# Exercise 8-16: Imports
# Take one of your earlier functions and store it in a separate module file.
# Then import it into this file using all five import styles:
#   1. import module_name
#   2. from module_name import function_name
#   3. from module_name import function_name as fn
#   4. import module_name as mn
#   5. from module_name import *

# TODO: Create a module file (e.g., my_functions.py) with one function
# TODO: Demonstrate all 5 import styles in this file
import my_functions
from my_functions import make_pizza
from my_functions import make_pizza as fn
import my_functions as mn
from my_functions import *


my_functions.make_pizza(12, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
fn(12, 'pepperoni')
mn.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
