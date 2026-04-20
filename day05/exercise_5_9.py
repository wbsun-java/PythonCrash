# Exercise 5-9: No Users
# Start with your exercise_5_8.py code.
# Add an if test BEFORE the loop to check if the list is empty.
# - If empty: print "We need to find some users!"
# - If not empty: run the greeting loop
# Then test with an empty list too.

users = ['admin', 'alice', 'bob', 'charlie', 'diana']

# TODO: Add an if check for empty list before the loop
if users == []:
    print("We need to find some users!")
else:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
