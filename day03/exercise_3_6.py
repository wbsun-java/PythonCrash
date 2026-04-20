# Exercise 3-6: More Guests
# Start with your program from Exercise 3-4 or 3-5.
# Add a print() call to inform people that you found a bigger dinner table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.
guests = ['Alice', 'Bob', 'Charlie']
print(f"Dear {guests[0]}, you are invited to dinner.")
print(f"Dear {guests[1]}, you are invited to dinner.")
print(f"Dear {guests[2]}, you are invited to dinner.")
print("I found a bigger dinner table!")
guests.insert(0, 'David')
guests.insert(2, 'Eve')
guests.append('Frank')
print("Dear " + guests[0] + ", you are invited to dinner.")
print("Dear " + guests[1] + ", you are invited to dinner.")
print("Dear " + guests[2] + ", you are invited to dinner.")
print("Dear " + guests[3] + ", you are invited to dinner.")
print("Dear " + guests[4] + ", you are invited to dinner.")
print("Dear " + guests[5] + ", you are invited to dinner.")