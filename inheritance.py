class Car():
   """A simple attempt to represent a car."""
   def __init__(self, make, model, year):
     self.make = make
     self.model = model
     self.year = year
     self.odometer_reading = 0

   def get_descriptive_name(self):
       long_name = str(self.year) + ' ' + self.make + ' ' + self.model
       return long_name.title()

   def read_odometer(self):
       print("This car has " + str(self.odometer_reading) + " miles on it.")

   def update_odometer(self, mileage):
       if mileage >= self.odometer_reading:
          self.odometer_reading = mileage

       else:
           print("You can't roll back an odometer!")

   def increment_odometer(self, miles):
        self.odometer_reading += miles

"""
Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 85 if it isn't already.
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery. You should
see an increase in the car's range.

"""
class Battery():
   """A simple attempt to model a battery for an electric car."""

   def __init__(self, battery_size=70):
    """Initialize the battery's attributes."""
    self.battery_size = battery_size

   def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

   def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
          range = 240
        elif self.battery_size == 85:
          range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)    

   def upgrade_battery(self):
     if self.battery_size != 85:
        self.battery_size = 85
        print("Battery upgraded to 85.")
     else:
        print("Battery is already at 85.")  

           

        

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
        
    def __init__(self, make, model, year):
         """Initialize attributes of the parent class."""
         super().__init__(make, model, year)
         self.battery1 = Battery()

             

my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery1.describe_battery()
# my_tesla.battery1.battery_size = int(input("Enter appropriate battery size: "))
# print(f"The battery size of the {my_tesla.model} model of the {my_tesla.make.title()} car is {my_tesla.battery1.battery_size}-kWh battery")
my_tesla.battery1.get_range()
my_tesla.battery1.upgrade_battery()
my_tesla.battery1.get_range()

