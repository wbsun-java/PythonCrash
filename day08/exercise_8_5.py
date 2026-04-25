# Exercise 8-5: Cities
# Write a function called describe_city()
# that accepts a city name and its country.
# Give the country parameter a default value (e.g., 'china').
# Print: "[City] is in [Country]."
# Call for three different cities; at least one not in the default country.

# TODO: Define describe_city(city, country='china')
def describe_city(city, country='china'):
    print(f"{city} is in {country}.")


# TODO: Call it for three cities
describe_city(city='Beijing', country='China')
describe_city(city='New York', country='USA')
describe_city(city='London', country='UK')
