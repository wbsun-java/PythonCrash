# Exercise 8-17: Styling Functions
# Choose any 3 programs you wrote for Chapter 8 and make sure they follow
# the PEP 8 styling guidelines for functions:
# - Descriptive function names (snake_case)
# - Two blank lines between top-level functions
# - Default values: no spaces around = (e.g., size='large')
# - Keyword args in calls: no spaces around = (e.g., make_shirt(size='medium'))
# - Keep lines under 79 characters
#
# This is a review exercise — look back at your ch8 files and clean up styling.
# No new code needed here unless you want to
# consolidate your cleaned-up versions.

# TODO: Review and polish 3 of your Chapter 8 exercises for PEP 8 compliance
def make_car(manufacturer, model, **options):
    """
    Make a dictionary representing a car.
    """
    car = {
        'manufacturer': manufacturer,
        'model': model
    }
    for key, value in options.items():
        car[key] = value
    return car


car = make_car(
    'subaru', 'outback',
    color='blue',
    year=2022,
    tow_package=True
)

for key, value in car.items():
    print(f"{key.title()}: {str(value).title()}")
print('\n')


def make_pizza(size, *toppings):
    """
    Summarize the pizza.
    """
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
make_pizza(12, 'pepperoni')
print('\n')


def build_profile(first, last, **user_info):
    """
    Build a dictionary containing everything we know about a user.
    """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


my_profile = build_profile(
    'albert',
    'einstein',
    location='princeton',
    field='physics'
)

print(my_profile)
print("\n")


def make_shirt(size, message):
    """
    Summarize the shirt.
    """
    print(f"\nMaking a {size}-inch shirt with the following message:")
    print(f"{message}")


make_shirt(16, 'Hello World')
make_shirt(12, 'Hello World')
print("\n")


def make_shirt(size='large', message='I love Python'):
    """
    Summarize the shirt.
    """
    print(f"\nMaking a {size}-inch shirt with the following message:")
    print(f"{message}")


make_shirt()
make_shirt(size='medium')
make_shirt(message='I love Python!!!')
print("\n")
