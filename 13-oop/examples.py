"""
Topic 13 - Object-Oriented Programming
Runnable examples matching the README.
"""


# Example 1: a basic class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")


my_dog = Dog("Rex", 3)
print(my_dog.name)
print(my_dog.age)
my_dog.bark()
# Expected output:
# Rex
# 3
# Rex says Woof!

# Example 2: multiple objects from the same class
dog1 = Dog("Rex", 3)
dog2 = Dog("Bella", 5)
dog1.bark()
dog2.bark()
# Expected output:
# Rex says Woof!
# Bella says Woof!


# Example 3: a method that computes something from attributes
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rect = Rectangle(4, 5)
print(rect.area())
# Expected output: 20


# Example 4: inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")


generic_animal = Animal("Creature")
my_cat = Cat("Whiskers")
generic_animal.speak()
my_cat.speak()
# Expected output:
# Creature makes a sound.
# Whiskers says Meow!
