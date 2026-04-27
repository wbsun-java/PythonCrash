# Exercise 9-3: Users
# Create a class called User with:
# - Attributes: first_name, last_name,
# and several more (e.g., age, email, location)
# - describe_user(): prints a summary of all the user's info
# - greet_user(): prints a personalized greeting
#
# Create several instances and call both methods on each.

# TODO: Define the User class with multiple attributes and two methods
class User:
    def __init__(self, first_name, last_name, age, email='', location=''):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"First Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location.title()}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")


# TODO: Create 2-3 instances and demonstrate both methods
new_user1 = User(
    first_name='john',
    last_name='smith',
    age=25
    )
new_user1.describe_user()
new_user1.greet_user()
print("\n")

new_user2 = User(
    first_name='jane',
    last_name='doe',
    location='los angeles',
    age=30
    )
new_user2.describe_user()
new_user2.greet_user()
print("\n")

new_user3 = User(
    first_name='bob',
    last_name='sage',
    age=35,
    email='bobsage@hotmail.com',
    location='beijing'
    )
new_user3.describe_user()
new_user3.greet_user()
print("\n")
