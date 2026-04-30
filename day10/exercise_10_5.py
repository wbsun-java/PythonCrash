# Exercise 10-5: Programming Poll
# Write a while loop that asks people why they like programming.
# Append each response to a file.
# Exit when user types 'quit'.

# TODO: While loop asking for a reason
while True:
    reason = input("Why do you like programming? ")
    if reason == 'quit':
        break
# TODO: Append each reason to a responses file
    with open('programming_poll.txt', 'a') as file_object:
        file_object.write(f"{reason}\n")

print()
