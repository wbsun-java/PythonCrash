# Exercise 9-14: Dice
# Use random.randint() to simulate dice rolls.
# Create a class called Die with:
# - Attribute: sides (default = 6)
# - Method: roll_die() — prints a random number from 1 to sides
#
# Make a 6-sided die and roll it 10 times.
# Make a 10-sided die and roll it 10 times.
# Make a 20-sided die and roll it 10 times.

from random import randint


# TODO: Define Die class with sides attribute and roll_die() method
class Dice():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


# TODO: Create 6-sided, 10-sided, and 20-sided dice and roll each 10 times
d6 = Dice()
d10 = Dice(sides=10)
d20 = Dice(sides=20)

print(f"D6: {d6.roll_die()}")
print(f"D10: {d10.roll_die()}")
print(f"D20: {d20.roll_die()}")
print("\n")

for _ in range(10):
    print(f"D6: {d6.roll_die()}")
print("\n")

for _ in range(10):
    print(f"D10: {d10.roll_die()}")
print("\n")

for _ in range(10):
    print(f"D20: {d20.roll_die()}")
print("\n")
