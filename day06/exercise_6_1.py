# Exercise 6-1: Person
# Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city they live in.
# Keys: first_name, last_name, age, city
# Print each piece of information stored in your dictionary.

# TODO: Create a dictionary called 'person' with
# first_name, last_name, age, city
# TODO: Print each value individually
friends = {
    'white': {
        'first_name': 'john',
        'last_name': 'white',
        'age': 25,
        'city': 'london',
    },
    'chris': {
        'first_name': 'chris',
        'last_name': 'willets',
        'age': 40,
        'city': 'paris',
    },
    'smith': {
        'first_name': 'smith',
        'last_name': 'mcconnel',
        'age': 45,
        'city': 'new york',
    },
}

for name, info in friends.items():
    print(f"{name.title()}:")
    full_name = f"{info['first_name']} {info['last_name']}"
    age = info['age']
    city = info['city']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tAge: {age}")
    print(f"\tCity: {city.title()}")
    print()

one_friend = {
    'first_name': 'john',
    'last_name': 'white',
    'age': 25,
    'city': 'london',
}
print(one_friend)
print(f"First Name: {one_friend['first_name'].title()}")
print(f"Last Name: {one_friend['last_name'].title()}")
print(f"Age: {one_friend['age']}")
print(f"Location: {one_friend['city'].title()}")
