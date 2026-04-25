# Exercise 8-13: User Profile
# Write a function called build_profile() that accepts first name, last name,
# and an arbitrary number of keyword arguments (**user_info).
# Return a dict with all the user's info.
# Call it with your own name and at least 3 extra key-value pairs.

# TODO: Define build_profile(first, last, **user_info) that returns a dict
def build_profile(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last, **user_info}
    for key, value in user_info.items():
        profile[key] = value
    return profile


# TODO: Call with your name and 3+ additional keyword arguments
user = build_profile(
    first='john',
    last='white',
    field='physics',
    occupation='director',
    age=53
)
# TODO: Print the returned profile
print(user)
