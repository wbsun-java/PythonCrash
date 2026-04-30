# Exercise 9-11: Imported Admin
# Store User, Privileges, and Admin classes in one module 
# (e.g., user_admin.py).
# In this file, import Admin and create an instance.
# Call show_privileges() to confirm everything works.

from user_admin import Admin


# TODO: Create user_admin.py with User, Privileges, and Admin classes
# TODO: In this file: from user_admin import Admin

# TODO: Create an Admin instance and call show_privileges()
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
new_admin.show_privileges()
print("\n")
