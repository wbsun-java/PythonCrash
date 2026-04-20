# Chapter 6 — Dictionaries
# Key examples from the book

# --- Creating and accessing a dictionary ---
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])    # green
print(alien_0['points'])   # 5

# --- Adding / modifying key-value pairs ---
alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0     # add new key
alien_0['y_position'] = 25
alien_0['color'] = 'yellow'   # modify existing key
print(alien_0)

# --- Removing a key-value pair ---
alien_0 = {'color': 'green', 'points': 5, 'speed': 'slow'}
del alien_0['points']
print(alien_0)

# --- get() to avoid KeyError ---
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)   # No point value assigned.

# --- Looping through key-value pairs ---
user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# --- Looping through keys only ---
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())

# --- Looping through values only ---
for language in favorite_languages.values():
    print(language.title())

# --- Looping through sorted keys ---
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# --- Nesting: list of dictionaries ---
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# --- Nesting: list inside a dictionary ---
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

# --- Nesting: dictionary inside a dictionary ---
users = {
    'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'princeton'},
    'mcurie':    {'first': 'marie',  'last': 'curie',    'location': 'paris'},
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {user_info['location'].title()}")
