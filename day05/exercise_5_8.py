# Exercise 5-8: Hello Admin
# Make a list of 5+ usernames including 'admin'.
# Loop through the list and greet each user:
# - 'admin': "Hello admin, would you like to see a status report?"
# - Everyone else: "Hello [name], thank you for logging in again."

users = ['admin', 'alice', 'bob', 'charlie', 'diana']

# TODO: Loop through users and print the appropriate greeting for each
for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")
