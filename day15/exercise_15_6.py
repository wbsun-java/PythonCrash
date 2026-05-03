# Exercise 15-6: Two D8s
# Roll two 8-sided dice 50,000 times and plot the frequency of each possible total.
#
# Steps:
# 1. Create a Die class with __init__(num_sides=6) and roll() → randint(1, num_sides)
# 2. Create two Die(8) instances
# 3. Roll both 50,000 times, add the results: results = [d1.roll() + d2.roll() for _ in range(50000)]
# 4. Count frequencies for each value from 2 to 16
# 5. Plot as a bar chart using plotly: Bar(x=x_values, y=frequencies)
# 6. Save to two_d8.html
#
# TODO: Create Die class
# TODO: Generate results for two D8s
# TODO: Count frequencies and plot with plotly

from random import randint

# TODO: Define Die class here

# TODO: Create two Die(8) instances and roll 50,000 times
# TODO: Count frequencies and plot
