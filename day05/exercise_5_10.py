# Exercise 5-10: Checking Usernames
# Simulate a website checking for unique usernames.
# - current_users: list of 5 existing usernames
# - new_users: list of 5 new usernames (1-2 overlap with current_users)
# Loop through new_users:
#   - If username already taken: "You'll need to enter a new username."
#   - If available: "That username is available."
# Make comparison case-insensitive (use .lower())

current_users = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
new_users = ['Frank', 'alice', 'George', 'bob', 'Hannah']

# TODO: Loop through new_users and
# check against current_users (case-insensitive)
for new_user in new_users:
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            print(f"{new_user.title()} is already taken. "
                  "You'll need to enter a new username.")
            break

    else:
        print(f"{new_user.title()}, that username is available.")
