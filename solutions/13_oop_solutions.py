"""
Solutions for 13 - Object-Oriented Programming
Try the exercises yourself first! (exercises/13_oop_exercises.py)
"""


# 1. Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


# 2. Car class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def describe(self):
        print(f"{self.year} {self.brand} {self.model}")


# 3. BankAccount class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


# 4. two Person objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
person1.introduce()
person2.introduce()


# 5. Student class with average()
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Carla", [85, 90, 78])
print(student.average())


# Challenge 1: BankAccount that refuses over-withdrawal
class SafeBankAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount


account = SafeBankAccount(100)
account.withdraw(150)
account.withdraw(50)
print(account.balance)


# Challenge 2: Shape base class with Circle/Square subclasses
class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


print(Circle(3).area())
print(Square(4).area())
