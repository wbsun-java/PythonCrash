# Exercise 7-5: Movie Tickets
# A movie theater charges based on age:
# - Under 3: free
# - 3 to 12: $10
# - Over 12: $15
# Write a loop that asks users their age, then tells them the ticket cost.
# Stop when user enters 'quit'.

# TODO: Write a while loop asking for age
while True:
    age = input("Enter your age: ")
    if age == 'quit':
        break
# TODO: Use if/elif/else to determine ticket price
    if int(age) < 4:
        price = 0
    elif int(age) <= 12:
        price = 10
    else:
        price = 15
# TODO: Print the price, exit on 'quit'
    print(f"Your ticket price is ${price}.")
