# Exercise 3-9: Dinner Guests
# Working with one of the programs from Exercises 3-4 through 3-7,
# use len() to print a message indicating the number of people you are inviting to dinner.
guests = ['Alice', 'Bob', 'Charlie']
print("I am inviting " + str(len(guests)) + " people to dinner.")
print(sorted(guests, reverse=False))
print(sorted(guests, reverse=True))

print("Orginal list: ")
print(guests)

guests.reverse()
print("Reversed list: ")
print(guests)

guests.sort()
print("Sorted list: ")
print(guests)

guests.sort(reverse=True)
print("Reverse-sorted list: ")
print(guests)

guests.append('Sun')
print(guests)

guests.insert(0, 'John')
print(guests)

del guests[1]
print(guests)

guests.pop()
print(guests)

print("There are " + str(len(guests)) + " guests in the list.")
