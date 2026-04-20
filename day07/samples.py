# Chapter 7 — User Input and while Loops
# Key examples from the book

# --- input() ---
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# --- Converting input to int ---
# age = input("How old are you? ")
# age = int(age)
# if age >= 18:
#     print("You can vote!")

# --- Modulo to check even/odd ---
number = 10
print(number % 3)   # 1  (remainder when dividing 10 by 3)

# --- Basic while loop ---
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# --- Loop with quit value ---
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# --- Flag (active variable) ---
active = True
count = 0
while active:
    count += 1
    if count >= 3:
        active = False   # flip the flag to exit
print("Loop ended after", count, "iterations")

# --- break ---
cities = ['beijing', 'london', 'tokyo', 'sydney']
for city in cities:
    if city == 'tokyo':
        break
    print(city.title())
print("Loop ended")

# --- continue ---
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue   # skip even numbers
    print(current_number)   # prints only odd numbers

# --- Moving items between lists with while ---
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for user in confirmed_users:
    print(user.title())

# --- Removing all instances of a value ---
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'dog']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# --- Storing input in a dictionary (commented — requires user input) ---
# responses = {}
# polling_active = True
# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
#     responses[name] = response
#     repeat = input("Would you like to let another person respond? (yes/no) ")
#     if repeat == 'no':
#         polling_active = False
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")
