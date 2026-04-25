# Exercise 8-14: Cars
# Write a function called make_car() that takes manufacturer and
# model (required),
# plus an arbitrary number of keyword arguments (**options).
# Return a dictionary with all the car info.
# Example call: car = make_car('subaru', 'outback',
#               color='blue', tow_package=True)
# Print the returned dictionary.

# TODO: Define make_car(manufacturer, model, **options)
def make_car(manufacturer, model, **options):
    car = {
        'manufacturer': manufacturer,
        'model': model
    }
    for key, value in options.items():
        car[key] = value
    return car


# TODO: Call it and print the result
car_1 = make_car(
    'subaru', 'outback',
    color='blue',
    year=2022,
    tow_package=True
    )

for key, value in car_1.items():
    print(f"{key.title()}: {str(value).title()}")
print('\n')

car_2 = make_car(
    'honda', 'accord',
    color='black',
    year=2022,
    sun_roof=True
)

for key, value in car_2.items():
    print(f"{key.title()}: {str(value).title()}")
print('\n')

car_3 = make_car(
    'toyota', 'corolla',
    color='red',
    year=2021,
    sun_roof=True,
    navigation=True
)

for key, value in car_3.items():
    print(f"{key.title()}: {str(value).title()}")
print('\n')


car_4 = make_car(
    'ford', 'f-150',
    color='red',
    year=2022,
    sun_roof=True,
    navigation=True,
    tow_package=True
)

for key, value in car_4.items():
    print(f"{key.title()}: {str(value).title()}")
