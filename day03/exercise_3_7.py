# Exercise 3-7: Shrinking Guest List
# Start with your program from Exercise 3-6.
# Add a print() call saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain.
# Each time you pop a name from your list, print a message to that person
# letting them know you're sorry you can't invite them to dinner.
# Print a message to each of the two people still on your list, letting them know
# they're still invited.
# Use del to remove the last two names from your list, so you have an empty list.
# Print your list to make sure you actually have an empty list at the end of your program.
guest_list = ['David', 'Alice', 'Eve', 'Bob', 'Charlie', 'Frank']
print("I can only invite two people for dinner.")
popped_guest = guest_list.pop()
print("Sorry " + popped_guest + ", I can't invite you to dinner.")
print(guest_list)
popped_guest = guest_list.pop()
print("Sorry " + popped_guest + ", I can't invite you to dinner.")
print(guest_list)
popped_guest = guest_list.pop()
print("Sorry " + popped_guest + ", I can't invite you to dinner.")
print(guest_list)
popped_guest = guest_list.pop()
print("Sorry " + popped_guest + ", I can't invite you to dinner.")
print(guest_list)
print("Dear " + guest_list[0] + ", you are still invited to dinner.")
print("Dear " + guest_list[1] + ", you are still invited to dinner.")
del guest_list[0]
del guest_list[0]
print(guest_list)
