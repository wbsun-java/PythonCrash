# Exercise 6-2: Favorite Numbers
# Use a dictionary to store people's favorite numbers.
# Think of five names as keys,
# and store a favorite number for each as the value.
# Print each person's name and their favorite number.

# TODO: Create a dictionary with 5 people and their favorite numbers
# TODO: Print each person's name and favorite number
people = {
    'john': {
        'first_name': 'john',
        'last_name': 'white',
        'favorite_number': 7
    },
    'chris': {
        'first_name': 'chris',
        'last_name': 'willets',
        'favorite_number': 6
    },
    'bob': {
        'first_name': 'bob',
        'last_name': 'smith',
        'favorite_number': 5
    },
    'sue': {
        'first_name': 'sue',
        'last_name': 'willets',
        'favorite_number': 4
    },
    'lisa': {
        'first_name': 'lisa',
        'last_name': 'conner',
        'favorite_number': 3
    }
}

for name, info in people.items():
    print(f"{name.title()}:")
    full_name = f"{info['first_name']} {info['last_name']}"
    fav_number = info['favorite_number']
    print(f"Full name: {full_name.title()}")
    print(f"Favorite Number: {fav_number}")
    print("")

fav_num = {
    'john': 7,
    'chris': 6,
    'bob': 5,
    'sue': 4,
    'lisa': 3
}

for name, number in fav_num.items():
    print(f"{name.title()}'s favorite number is: {number}")
