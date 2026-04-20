# Exercise 4-4: One Million
# Make a list of the numbers from 1 to 1,000,000, then use a for loop to
# print the numbers. (If the output takes too long, stop by pressing CTRL-C.)

numbers = list(range(1, 1_000_001))
for number in numbers:
    print(number)
