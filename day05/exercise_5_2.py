# Exercise 5-2: More Conditional Tests
# You don't have to limit the number of tests you create to 10.
# Try these tests:
# - Tests for equality and inequality with strings
# - Tests using lower() to ignore case
# - Numerical tests: ==, !=, >, <, >=, <=
# - Tests using 'and' and 'or'
# - Test whether an item is in a list
# - Test whether an item is not in a list

# TODO: Write at least one test for each type listed above
drink = 'coke'
print("\nIs drink == 'coke'? I predict True.")
print(drink.lower() == 'coke')

print("\nIs drink == 'code'? I predict False.")
print(drink.upper() == 'water')

number = 10
print("\nIs number == 10? I predict True.")
print(number == 10)
print("\nIs number == 10? I predict False.")
print(number == 12)
print("\nIs number != 10? I predict False.")
print(number != 10)
print("\nIs number >=9 and number == 11? I predict False.")
print(number >= 9 and number == 11)
print("\nIs number >=9 or number <= 11? I predict True.")
print(number >= 9 or number <= 11)


car = ('audi', 'bmw', 'subaru', 'toyota')
print(car)
print("\nIs 'bmw' in car? I predict True.")
print('bmw' in car)

print("\nIs 'toyota' in car? I predict True.")
print('toyota' in car)

print("\nIs 'ford' not in car? I predict True.")
print('ford' not in car)

print("\nIs 'subaru' not in car? I predict False.")
print('subaru' not in car)
