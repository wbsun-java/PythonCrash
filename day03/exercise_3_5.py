# Exercise 3-5: Changing Guest List
# Start with your program from Exercise 3-4.
# Add a print() call at the end of your program stating the name of the guest
# who can't make it.
# Modify your list, replacing the name of the guest who can't make it with the
# name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.
guest_list = ['Albert Einstein', 'Marie Curie', 'Isaac Newton']
print("Dear " + guest_list[0] + ", you are cordially invited to dinner.")
print("Dear " + guest_list[1] + ", you are cordially invited to dinner.")
print("Dear " + guest_list[2] + ", you are cordially invited to dinner.")
print("\nUnfortunately, " + guest_list[1] + " can't make it to dinner.")
guest_list[1] = 'Nikola Tesla'
print("\nDear " + guest_list[0] + ", you are cordially invited to dinner.")
print("Dear " + guest_list[1] + ", you are cordially invited to dinner.")
print("Dear " + guest_list[2] + ", you are cordially invited to dinner.")
