from user import User


class Privileges():
    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, location=''):
        super().__init__(first_name, last_name, age, location)
        self.access = Privileges()

    def show_privileges(self):
        self.access.show_privileges()
