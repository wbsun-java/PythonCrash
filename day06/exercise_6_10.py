# Exercise 6-10: Favorite Numbers (multiple)
# Modify Exercise 6-2 so each person can have MORE THAN ONE favorite number.
# Each value should now be a LIST of numbers.
# Print each person's name along with their favorite numbers.

# TODO: Create a dictionary where each value is a LIST of favorite numbers
favorite_numbers = {
    'john': {
        'first_name': 'john',
        'last_name': 'white',
        'favorite_numbers': [7, 6, 5]
    },
    'lisa': {
        'first_name': 'lisa',
        'last_name': 'conner',
        'favorite_numbers': [4, 3, 2, 1]
    },
    'sue': {
        'first_name': 'sue',
        'last_name': 'willets',
        'favorite_numbers': [10]
    },
    'bob': {
        'first_name': 'bob',
        'last_name': 'smith',
        'favorite_numbers': [11, 12, 13]
    },
    'chris': {
        'first_name': 'chris',
        'last_name': 'willets',
        'favorite_numbers': [14, 15, 16]
    }
}
# TODO: Loop and print each person's name and their list of numbers
for name, info in favorite_numbers.items():
    print(f"{name.title()}:")
    full_name = f"{info['first_name'].title()} {info['last_name'].title()}"
    fav_numbers = info['favorite_numbers']
    print(f"Full Name: {full_name}")
    print("Favorite Numbers: ")
    for number in fav_numbers:
        print(f"    {number}")
    print()
