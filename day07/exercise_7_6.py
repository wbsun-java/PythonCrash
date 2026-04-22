# Exercise 7-6: Three Exits
# Write three versions of Exercise 7-4 or 7-5,
# each using a different exit strategy:
# Version 1: Use a conditional test in the while statement to stop the loop
# Version 2: Use an active variable (flag) to control the loop
# Version 3: Use a break statement to exit when user enters 'quit'

# --- Version 1: conditional test in while ---
age = ''
while age != 'quit':
    age = input("Enter your age: ")
    if age != 'quit':
        if int(age) < 4:
            price = 0
        elif int(age) <= 12:
            price = 10
        else:
            price = 15
    print(f"Your ticket price is ${price}.")

# --- Version 2: active variable / flag ---
active = True
while active:
    age = input("Enter your age: ")
    if age == 'quit':
        active = False
    else:
        if int(age) < 4:
            price = 0
        elif int(age) <= 12:
            price = 10
        else:
            price = 15
    print(f"Your ticket price is ${price}.")

# --- Version 3: break statement ---
while True:
    age = input("Enter your age: ")
    if age == 'quit':
        break
    if int(age) < 4:
        price = 0
    elif int(age) <= 12:
        price = 10
    else:
        price = 15
    print(f"Your ticket price is ${price}.")
