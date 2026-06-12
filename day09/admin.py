from user import User


class Privileges:
    def __init__(self):
        self.privileges = []

    def set_privileges(self):
        while True:
            privilege = input("Enter a privilege: (q to quit)")
            if privilege != 'q':
                self.privileges.append(privilege)
            else:
                break

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")


class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()


admin = Admin('john', 'doe', 30, 'los angeles')
admin.user_decription()
admin.greet_user()
admin.privileges.set_privileges()
admin.privileges.show_privileges()
print("\n")
