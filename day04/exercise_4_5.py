# Exercise 4-5: Summing a Million
# Make a list of the numbers from 1 to 1,000,000.
# Use min(), max(), and sum() to print statistics about your list.

numbers = list(range(1, 1_000_001))
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sum: {sum(numbers)}")
