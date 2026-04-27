# Exercise 9-8: Privileges
# Create a separate Privileges class with:
# - Attribute: privileges (list of strings)
# - Method: show_privileges()
#
# In your Admin class (from 9-7), replace the privileges list with a
# Privileges INSTANCE as an attribute.
# Create an Admin instance and call admin.privileges.show_privileges().
from exercise_9_3 import User


# TODO: Define Privileges class with privileges list and show_privileges()
class Privileges():
    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# TODO: Define Admin(User) with self.privileges = Privileges([...])
class Admin(User):
    def __init__(self, first_name, last_name, age, email='', location=''):
        super().__init__(first_name, last_name, age, email, location)
        self.access = Privileges()

    def show_privileges(self):
        self.access.show_privileges()

    # Define show_privileges in method
    def method_show_privileges(self):
        for p in self.access.privileges:
            print(f"- {p}")


# TODO: Create an Admin instance and call show_privileges()
# via the nested object
new_admin = Admin(
    first_name='john',
    last_name='doe',
    age=30,
    email='sample@gmail.com',
    location='los angeles'
)

new_admin.describe_user()
new_admin.greet_user()
new_admin.access.privileges = [
    "can add uers",
    "can delete users",
    "can ban user"
]
print("Nested object way: ")
new_admin.show_privileges()
print("\nPrint method way: ")
new_admin.method_show_privileges()
print("\n")
