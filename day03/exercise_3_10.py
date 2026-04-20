# Exercise 3-10: Every Function
# Think of things you could store in a list.
# For example, you could make a list of mountains, rivers, countries, cities, languages,
# or anything else you'd like.
# Write a program that creates a list containing these items and then uses each function
# introduced in this chapter at least once.
places = ['Paris', 'Tokyo', 'New York', 'Sydney', 'Rome']

print("Original list:")
print(places)

print("Sorted list:")
print(sorted(places))

print("Original list still unchanged:")
print(places)

print("Sorted list in reverse order:")
print(sorted(places, reverse=True))

print("Original list still unchanged:")
print(places)

places.reverse()
print("Reversed list:")
print(places)

places.reverse()
print("Back to original order:")
print(places)

places.sort()
print("Sorted list:")
print(places)

places.sort(reverse=True)
print("Reverse-sorted list:")
print(places)

places.append('London')
print("After append:")
print(places)

places.insert(0, 'Berlin')
print("After insert:")
print(places)

del places[0]
print("After del:")
print(places)

places.pop()
print("After pop:")
print(places)

print("First item:")
print(places[0])

print("There are " + str(len(places)) + " places in the list.")
