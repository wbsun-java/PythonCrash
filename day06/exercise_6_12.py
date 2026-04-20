# Exercise 6-12: Extensions
# Take any example or exercise from Chapter 6 and extend it.
# Ideas: add new keys/values, change the context, improve the formatting.
# This is a creative exercise — make it your own!

# TODO: Choose one of your Chapter 6 programs and 
# extend it in an interesting way
extensions = {
    'new york': {
        'country': 'USA',
        'population': '8.4 million',
        'fact1': 'The Statue of Liberty was a gift from France',
        'fact2': 'Central Park is larger than Monaco.',
        'fact3': 'Times Square is one of the most expensive advertising'
                 ' markets in the world.',
        'fact4': 'There are more billionaires in New York than'
                 ' any other city in the world.',
    },
    'london': {
        'country': 'UK',
        'population': '8.9 million',
        'fact1': 'The London Underground is the oldest in the world',
        'fact2': 'The city has more than 170 museums.',
        'fact3': 'Buckingham Palace has 775 rooms.',
        'fact4': 'London has 68 unique tube stations.'
    },
    'tokyo': {
        'country': 'Japan',
        'population': '13.9 million',
        'fact1': 'The Shibuya Crossing is the busiest intersection '
                 'in the world',
        'fact2': 'Japan has one of the highest life expectancies'
                 ' in the world.',
        'fact3': 'Tokyo is the most populous metropolitan area '
                 'in the world.',
        'fact4': 'The first 7-Eleven outside of the U.S. opened '
                 'in Tokyo in 1974.',
    },
}

for city, info in extensions.items():
    print(city.title())
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact 1: {info['fact1']}")
    print(f"  Fact 2: {info['fact2']}")
    print(f"  Fact 3: {info['fact3']}")
    print(f"  Fact 4: {info['fact4']}")
    print()
