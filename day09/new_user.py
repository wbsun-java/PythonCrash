from dataclasses import dataclass


@dataclass
class Newuser:
    first_name: str
    last_name: str
    age: int
    location: str = ''

    def describe_user(self):
        print(f"First Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location.title()}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")
