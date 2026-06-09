import datetime
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.used_years = 0
        self.limited_years = 5

    def get_describe_name(self, who):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {who} {self.make} {self.model}"
        return long_name.title()

    def use_age(self, used_years=None):
        """Print a statement show the car was use how long"""
        used_years = datetime.datetime.now().year - self.year
        if used_years == 0 or used_years is None:
            print(f"This car has used {self.used_years}")
        else:
            print(f"This car has used {used_years}")

    def update_use_age(self):
        """Judge and print the car over the use_age"""
        current_year = datetime.datetime.now().year
        years = current_year - self.year
        if years > self.limited_years:
            print(f"Your car is used {years} year,should be discard")
        else:
            print(f"Your car is used {years} year,can continue used")



my_car = Car('audi', 'a4', 2015)
print(my_car.get_describe_name("Mr Smith"))
my_car.use_age()
my_car.update_use_age()