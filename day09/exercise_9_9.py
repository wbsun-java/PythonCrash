# Exercise 9-9: Battery Upgrade
# Use the ElectricCar / Battery class concept from the chapter.
# Create a Battery class with:
# - Attribute: battery_size = 70
# - get_range(): prints estimated range based on battery size
# - upgrade_battery(): if battery_size is not 85, set it to 85
#
# Create an ElectricCar with a Battery.
# Call get_range(), then upgrade_battery(), then get_range() again.
# You should see the range increase.
from car import Car


# TODO: Define Battery class with battery_size, get_range(), upgrade_battery()
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def get_range(self):
        print(f"This car can go approximately {self.battery_size * 3}")

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


# TODO: Define ElectricCar class with a Battery instance
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def get_range(self):
        self.battery.get_range()

    def upgrade_battery(self):
        self.battery.upgrade_battery()


# TODO: Demonstrate upgrade and range change
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.odometer_reading = 23500
my_tesla.read_odometer()

my_tesla.get_range()
my_tesla.upgrade_battery()
my_tesla.get_range()
