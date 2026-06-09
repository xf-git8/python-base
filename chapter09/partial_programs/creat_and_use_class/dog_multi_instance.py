class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dod sitting in response to a command"""
        print(f"{self.age}岁的{self.name.title()} is now sitting")

    def rolled_over(self):
        """Simulate a dog rolling over in response to a command"""
        print(f"{self.age}岁的{self.name.title()} is rolled over")


my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

my_dog.sit()
my_dog.rolled_over()
print()
your_dog.sit()
your_dog.rolled_over()
