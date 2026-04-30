# Exercise 9-12: Multiple Modules
# Store User in one module (e.g., user.py).
# Store Privileges and Admin in a separate module (e.g., admin.py).
# In this file, import Admin and create an instance.
# Call show_privileges() to confirm everything works across multiple modules.

from admin import Admin


# TODO: Create user.py with just the User class
# TODO: Create admin.py with Privileges and Admin (importing User from user.py)
# TODO: In this file: from admin import Admin — then test it
new_admin = Admin(
    'john',
    'doe',
    30,
    'los angeles'
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
