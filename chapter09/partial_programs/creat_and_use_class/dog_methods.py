from pygments.lexers.sql import do_re


class Dog:
    """A simple attempt to model a don"""

    def __init__(self,name,age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog  sitting in response to a command """
        print(f"{self.name.title()} is now sitting")
    def roll_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(f"{self.name.title()} rolled over")
my_dog = Dog('willie',6)
my_dog.sit()
my_dog.roll_over()
