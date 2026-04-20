# Exercise 6-5: Rivers
# Make a dictionary with 3 major rivers as keys and the country 
# they run through as values.
# Example: {'nile': 'egypt', ...}
#
# Then write THREE separate loops:
# 1. Print a sentence about each river: "The Nile runs through Egypt."
# 2. Print the name of each river.
# 3. Print the name of each country.

rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'yangtze': 'china',
}

# TODO: Loop 1 - print a sentence about each river
print("Rivers and the countries they flow through:")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print()  # TODO: Loop 2 - print each river name
print("Rivers:")
for river in rivers:
    print(river.title())
print()  # TODO: Loop 3 - print each country name
print("Countries:")
for country in rivers.values():
    print(country.title())
