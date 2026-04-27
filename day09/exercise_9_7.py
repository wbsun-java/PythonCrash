# Exercise 9-7: Admin
# Write a class called Admin that inherits from User (Exercise 9-3 or 9-5).
# Add attribute: privileges — a list of strings like:
#   ["can add post", "can delete post", "can ban user"]
# Add a method show_privileges() that lists the admin's privileges.
# Create an Admin instance and call show_privileges().

# TODO: Define User base class (or copy from 9-3)
from exercise_9_3 import User


# TODO: Define Admin(User) with privileges list and show_privileges() method
class Admin(User):
    def __init__(self, first_name, last_name, age, email='', location=''):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = []

    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# TODO: Create an instance and call show_privileges()
new_admin = Admin(
    first_name='john',
    last_name='doe',
    age=30
)

new_admin.describe_user()
new_admin.greet_user()
new_admin.privileges = [
    "can add post",
    "can delete post",
    "can ban user"
]
new_admin.show_privileges()
print("\n")
