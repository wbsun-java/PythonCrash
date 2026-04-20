# Exercise 6-11: Cities
# Make a dictionary called 'cities' with 3 city names as keys.
# Each value is a dictionary with: country, population, fact.
# Print the name of each city and all the information stored about it.

# TODO: Create cities dict with 3 cities, each having country/population/fact
cities = {
    'new york': {
        'country': 'USA',
        'population': '8.4 million',
        'fact': 'The Statue of Liberty was a gift from France'
    },
    'london': {
        'country': 'UK',
        'population': '8.9 million',
        'fact': 'The London Underground is the oldest in the world'
    },
    'tokyo': {
        'country': 'Japan',
        'population': '13.9 million',
        'fact': 'The Shibuya Crossing is the busiest intersection in the world'
    }
}

# TODO: Loop through and print each city's name and all its info

for city, info in cities.items():
    print(f"City: {city.title()}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
    print()
