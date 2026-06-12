from new_user import Newuser


class New_admin(Newuser):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.access = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = New_admin('john', 'doe', 30)
admin.describe_user()
admin.greet_user()
admin.access.privileges = ['can add user', 'can delete user', 'can ban user']
admin.access.show_privileges()
print("\n")
