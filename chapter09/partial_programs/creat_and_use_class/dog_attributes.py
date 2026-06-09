class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attribute"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")
    def roll_over(self):
        """simulate a dog rolling over in response to a command"""
        print(f"{self.name} rolled voer" )
my_dog = Dog('willie',6)
your_dog= Dog('lucy',3)
print(f"My dog name is {my_dog.name.title()}")
print(f"My dog age is {my_dog.age}")