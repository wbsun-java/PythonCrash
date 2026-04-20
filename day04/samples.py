# Chapter 4 — Working with Lists
# Key examples from the book

# --- for loops ---
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

# --- range() ---
for value in range(1, 5):      # prints 1 2 3 4  (stops before 5)
    print(value)

numbers = list(range(1, 6))    # [1, 2, 3, 4, 5]
print(numbers)

even_numbers = list(range(2, 11, 2))   # step of 2
print(even_numbers)   # [2, 4, 6, 8, 10]

# --- Building a list with a loop ---
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# --- min / max / sum ---
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))   # 0
print(max(digits))   # 9
print(sum(digits))   # 45

# --- List comprehension (same as above in one line) ---
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# --- Slices ---
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])    # first three
print(players[1:4])    # middle
print(players[:3])     # from start
print(players[2:])     # to end
print(players[-3:])    # last three

for player in players[:3]:    # loop over a slice
    print(player.title())

# --- Copying a list (use [:] not =) ---
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]     # real copy
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)        # has cannoli, not ice cream
print(friend_foods)    # has ice cream, not cannoli

# --- Tuples (immutable) ---
dimensions = (200, 50)
print(dimensions[0])   # 200
# dimensions[0] = 250  # TypeError! tuples can't be changed

for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)    # you CAN reassign the variable
print(dimensions)
