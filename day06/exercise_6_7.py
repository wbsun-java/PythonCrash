# Exercise 6-7: People
# Build on Exercise 6-1.
# Create 3 dictionaries each representing a different person 
# (first_name, last_name, age, city).
# Store all three in a list called 'people'.
# Loop through people and print everything you know about each person

# TODO: Create 3 person dictionaries
person_1 = {
    'first_name': 'john',
    'last_name': 'white',
    'age': 25,
    'city': 'london',
}
person_2 = {
    'first_name': 'chris',
    'last_name': 'willets',
    'age': 40,
    'city': 'paris',
}
person_3 = {
    'first_name': 'smith',
    'last_name': 'mcconnel',
    'age': 45,
    'city': 'new york',
}

# TODO: Store them in a list called 'people'
people = [person_1, person_2, person_3]
# TODO: Loop through people and print all their info
for person in people:
    full_name = (person['first_name'].title() + " " +
                 person['last_name'].title())
    age = person['age']
    city = person['city'].title()

    print(f"Name: {full_name}")
    print(f"Age: {age}")
    print(f"Location: {city}")
    print()
