# Exercise 9-15: Python Module of the Week
# Visit https://pymotw.com/ and explore the Python standard library.
# Find an interesting module (or look at 'collections' or 'random').
# Write a short program that uses something from that module.
# Add a comment explaining what you found interesting.

# TODO: Import a module from the Python standard library
import datetime
# TODO: Write a small demo program using something from it


class BirthdayCalculation():
    def __init__(self, year, month, day):
        self.birth_date = datetime.date(year, month, day)

    def days_since_birth(self):
        today = datetime.date.today()
        delta = today - self.birth_date
        return delta.days


# Create a birthday instance (Example: January 1, 2000)
my_bday = BirthdayCalculation(1972, 1, 11)
my_days = my_bday.days_since_birth()
print(f"Days since birth: {my_days}")

her_bday = BirthdayCalculation(1977, 5, 29)
her_days = her_bday.days_since_birth()
print(f"Days since birth: {her_days}")

difference = my_days - her_days
print(f"Our difference in days: {difference}")

# TODO: Add a comment explaining what you found and why it's interesting
# I found the 'datetime' module interesting because it handles complex 
# calendar calculations (like leap years and varying month lengths) 
# automatically, making it easy to calculate time differences.
