# Exercise 6-6: Polling
# Given the favorite_languages dictionary below, 
# check who has and hasn't taken the poll.
# - people_to_poll: list of names (some already in dict, some not)
# - If already in dict: "Thank you for taking the poll, [name]!"
# - If not in dict: "We'd love to know your favorite language, [name]!"

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people_to_poll = ['jen', 'sarah', 'mike', 'edward', 'anna']

# TODO: Loop through people_to_poll and check if 
# each is already in favorite_languages
for name in people_to_poll:
    if name in favorite_languages:
        print(f"Thank you for taking the poll, {name.title()}!")
    else:
        print(f"We'd love to know your favorite language, {name.title()}!")
