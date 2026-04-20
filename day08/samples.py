# Chapter 8 — Functions
# Key examples from the book

# --- Defining and calling a function ---
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# --- Parameter / argument ---
def greet_user(username):
    """Display a personalized greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
greet_user('sarah')

# --- Keyword arguments ---
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')                    # positional
describe_pet(pet_name='harry', animal_type='hamster')  # keyword

# --- Default values ---
def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')          # uses default 'dog'
describe_pet('harry', 'hamster')  # overrides default

# --- Return value ---
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# --- Optional parameter with None ---
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

print(get_formatted_name('jimi', 'hendrix'))
print(get_formatted_name('john', 'hooker', 'lee'))

# --- Return a dictionary ---
def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

print(build_person('jimi', 'hendrix', age=27))

# --- Passing a list ---
def greet_users(names):
    for name in names:
        print(f"Hello, {name.title()}!")

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# --- Modifying a list inside a function vs. using a copy ---
def print_models(unprinted, completed):
    while unprinted:
        current = unprinted.pop()
        print(f"Printing model: {current}")
        completed.append(current)

unprinted = ['phone case', 'robot pendant', 'dodecahedron']
completed = []
print_models(unprinted, completed)
print("\nCompleted:", completed)

# Use a copy to protect the original:
original = ['phone case', 'robot pendant', 'dodecahedron']
completed2 = []
print_models(original[:], completed2)   # passes a copy
print("Original still intact:", original)

# --- *args (arbitrary positional arguments) ---
def make_pizza(*toppings):
    print("\nMaking a pizza with these toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# --- **kwargs (arbitrary keyword arguments) ---
def build_profile(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile

user = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user)

# --- Importing a module (for reference) ---
# import pizza
# pizza.make_pizza('large', 'pepperoni')
#
# from pizza import make_pizza
# make_pizza('large', 'pepperoni')
