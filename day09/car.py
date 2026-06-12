class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_meter(self):
        return self.odometer_reading

    def update_meter(self, mileage):
        self.odometer_reading = mileage


my_car = Car('toyota', '4runner', 2017)
print(my_car.get_descriptive_name())

my_car.odometer_reading = 23
print(my_car.read_meter())

my_car.update_meter(30)
print(my_car.read_meter())


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        else:
            range = round(240/70 * self.battery_size)
        print(f"This car can go about {range} miles on a full charge.")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.get_range()
my_tesla.upgrade_battery()
my_tesla.describe_battery()
my_tesla.get_range()
