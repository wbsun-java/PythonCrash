# Exercise 4-8: Cubes
# A number raised to the third power is called a cube.
# Make a list of the first 10 cubes (1, 8, 27, ...) using a for loop,
# and print each cube value.
# your loop here
# TODO: Loop through 1-10, calculate cube with **, append to a list, then print each

cubes = []
for value in range(1, 11):
    cubes.append(value ** 3)

for cube in cubes:
    print(cube)

cube1 = [value ** 3 for value in range(1, 11)]
print(cube1)
for value in cube1:
    print(value)
