# Exercise 5-11: Ordinal Numbers
# Store numbers 1-9 in a list.
# Loop through the list and use if-elif-else to print the ordinal:
# - 1 → "1st"
# - 2 → "2nd"
# - 3 → "3rd"
# - 4-9 → "4th", "5th", etc.

numbers = list(range(1, 10))

# TODO: Loop through numbers and print each with its ordinal suffix
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
