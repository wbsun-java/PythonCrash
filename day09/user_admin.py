class User():
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


class Privileges():
    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, email='', location=''):
        super().__init__(first_name, last_name, age, email, location)
        self.access = Privileges()

    def show_privileges(self):
        self.access.show_privileges()
