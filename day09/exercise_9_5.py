# Exercise 9-5: Login Attempts
# Add to your User class from Exercise 9-3:
# - Attribute: login_attempts = 0
# - increment_login_attempts(): increments login_attempts by 1
# - reset_login_attempts(): resets login_attempts to 0
#
# Create a User instance. Call increment_login_attempts() several times.
# Print login_attempts, then call reset_login_attempts() and print again.

# TODO: Define User class with login_attempts attribute and two methods
class User:
    def __init__(self, first_name, last_name, age, email='', location=''):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"First Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location.title()}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# TODO: Demonstrate incrementing and resetting
user_test = User('alice', 'wonderland', 22)

print("User's information: ")
user_test.describe_user()
user_test.greet_user()


print("Increamenting login attempts:")
user_test.increment_login_attempts()
user_test.increment_login_attempts()
user_test.increment_login_attempts()
print(f"Login Attempts: {user_test.login_attempts}")

print("Resetting login attempts:")
user_test.reset_login_attempts()
print(f"Login Attempts: {user_test.login_attempts}")
print("\n")
