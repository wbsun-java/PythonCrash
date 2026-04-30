# Exercise 10-13: Verify User
# Improve the remember_me.py pattern:
# When loading a stored username, ask the user to confirm it's correct.
# If correct: print a welcome-back message.
# If not correct: ask for the new correct username, save it, and greet them.

import json


def get_stored_username():
    """Return stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def get_new_username():
    """Prompt for a new username and save it."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    # TODO: Get the stored username
    username = get_stored_username()
    # TODO: If found, ask user to confirm it's them
    if username:
        # TODO: If confirmed, print a welcome-back message
        print(f"Are you {username.title()}? y/n")
    # TODO: If not confirmed, call get_new_username() and greet the new user
        if input() == 'y':
            print(f"Welcome back, {username.title()}!")
        else:
            username = get_new_username()
            print(f"Greeting! {username.title()}")
    # TODO: If no stored username, call get_new_username()and greet them
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username.title()}!")


greet_user()
