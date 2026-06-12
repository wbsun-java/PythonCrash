from dataclasses import dataclass


@dataclass
class Newcar:
    make: str
    model: str
    year: int
    meter_reading: int = 0

    def get_meter_reading(self, mileage):
        self.meter_reading = mileage
        return self.meter_reading


my_car = Newcar('toyota', '4runner', 2017)
print(my_car)
print(f"My car's meter reading is {my_car.get_meter_reading(23)}.")
my_car.get_meter_reading(30)


@dataclass
class ElectricCar(Newcar):
    battery_size: int = 70

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
print(my_tesla)
my_tesla.describe_battery()
my_tesla.get_range()
my_tesla.get_meter_reading(23500)
my_tesla.upgrade_battery()
my_tesla.get_range()
