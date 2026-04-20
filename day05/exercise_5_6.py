# Exercise 5-6: Stages of Life
# Set a value for age, then use if-elif-else to print the person's stage of life:
# - Less than 2: baby
# - 2 to 3: toddler
# - 4 to 12: kid
# - 13 to 19: teenager
# - 20 to 64: adult
# - 65 or older: elder

age = 25

# TODO: Write the if-elif-else chain for all six stages
if age < 2:
    print("You're a baby!")
elif age <= 3:
    print("You're a toddler!")
elif age <= 12:
    print("You're a kid!")
elif age <= 19:
    print("You're a teenager!")
elif age <= 64:
    print("You're an adult!")
else:
    print("You're an elder!")
