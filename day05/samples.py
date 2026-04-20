# Chapter 5 — if Statements
# Key examples from the book

# --- Simple if with a list ---
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# --- Comparison operators ---
age = 19
print(age == 19)    # True
print(age != 20)    # True
print(age < 21)     # True
print(age >= 18)    # True

# --- Case-insensitive comparison ---
car = 'Audi'
print(car.lower() == 'audi')   # True (original unchanged)

# --- and / or ---
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)   # False
print(age_0 >= 21 or age_1 >= 21)    # True

# --- in / not in ---
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)      # True
print('pepperoni' in requested_toppings)      # False

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# --- if / if-else ---
age = 19
if age >= 18:
    print("You are old enough to vote!")

age = 17
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")

# --- if-elif-else chain ---
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

# --- Multiple independent if statements (all are checked) ---
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("Finished making your pizza!")

# --- if with lists: check for empty list ---
requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print("Adding " + topping + ".")
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
