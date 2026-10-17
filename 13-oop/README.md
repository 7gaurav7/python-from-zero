# 13 — Object-Oriented Programming (OOP)

## 1. Beginner-Friendly Explanation

So far you've modeled data using plain variables, lists, and dictionaries.
**Object-Oriented Programming** offers another way: define a **class** — a
blueprint describing what a kind of "thing" has (its **attributes**) and
what it can do (its **methods**) — then create individual **objects**
(also called **instances**) from that blueprint.

Example: a `Dog` class might describe that every dog has a `name` and
`age`, and can `bark()`. Each individual dog object (`my_dog`,
`your_dog`) shares the same blueprint but has its own specific name and age.

## 2. Important Concepts

- **Class** — a blueprint/template for creating objects.
- **Object (instance)** — a specific thing created from a class.
- **Attribute** — a piece of data stored on an object (e.g. `name`).
- **Method** — a function defined inside a class, describing behavior.
- **`__init__`** — the special method that runs automatically when a new
  object is created; used to set up its initial attributes.
- **`self`** — refers to the specific object a method is being called on;
  always the first parameter of a method.
- **Inheritance** — a class can be based on another class, reusing and
  extending its behavior (e.g. `class Puppy(Dog):`).

## 3. Syntax

```python
class ClassName:
    def __init__(self, param1, param2):
        self.attribute1 = param1
        self.attribute2 = param2

    def some_method(self):
        return f"{self.attribute1} does something"

# Creating an object (instance)
obj = ClassName("value1", "value2")
obj.some_method()

# Inheritance
class ChildClass(ClassName):
    def __init__(self, param1, param2, extra):
        super().__init__(param1, param2)   # runs the parent's __init__
        self.extra = extra
```

## 4. Simple Examples

**Example 1 — A basic class**
```python
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
```
Expected output:
```
Rex
3
Rex says Woof!
```

**Example 2 — Multiple objects from the same class**
```python
dog1 = Dog("Rex", 3)
dog2 = Dog("Bella", 5)
dog1.bark()
dog2.bark()
```
Expected output:
```
Rex says Woof!
Bella says Woof!
```

**Example 3 — A method that uses attributes to compute something**
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(4, 5)
print(rect.area())
```
Expected output:
```
20
```

**Example 4 — Inheritance**
```python
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
```
Expected output:
```
Creature makes a sound.
Whiskers says Meow!
```

## 5. Practice Problems

1. Create a `Person` class with `name` and `age` attributes and a method
   `introduce()` that prints "Hi, I'm X and I'm Y years old."
2. Create a `Car` class with `brand`, `model`, and `year`, and a method
   `describe()` that prints a summary sentence.
3. Create a `BankAccount` class with a `balance` attribute and methods
   `deposit(amount)` and `withdraw(amount)` that update the balance.
4. Create two objects from your `Person` class with different names/ages
   and call `introduce()` on each.
5. Create a `Student` class with `name` and a list `grades`, and a method
   `average()` that returns the average grade.

## 6. Challenge Problems

1. Extend the `BankAccount` class so `withdraw()` refuses (and prints a
   message) if the requested amount is greater than the balance.
2. Create a base class `Shape` with a method `area()` that returns `0`, then
   create `Circle` and `Square` subclasses that each override `area()` with
   their own correct formula.

## 7. Common Mistakes

- **Forgetting `self`** as the first parameter of every method — Python
  will raise a `TypeError` about missing arguments.
- **Forgetting to call methods/attributes on an object**, e.g. writing
  `Dog.bark()` instead of `my_dog.bark()`.
- **Confusing the class (the blueprint) with an object (a specific instance)**
  — `Dog` describes all dogs; `my_dog` is one actual dog.
- **Not initializing an attribute in `__init__`**, then trying to use it in
  another method — causes an `AttributeError`.
- **Overriding `__init__` in a subclass without calling `super().__init__()`**
  when you still want the parent's setup logic to run.

## 8. Mini Quiz

1. What is the difference between a class and an object?
2. What special method runs automatically when you create a new object?
3. What does `self` refer to inside a method?
4. What keyword lets one class inherit from another?
5. How do you call a parent class's `__init__` from a child class?

*(Answers: 1. A class is the blueprint; an object is a specific thing created from it  2. `__init__`  3. The specific object the method is being called on  4. Put the parent class name in parentheses: `class Child(Parent):`  5. `super().__init__(...)`)*

## 9. Practical Exercise

Create `library_system.py` with a `Book` class (`title`, `author`,
`is_checked_out` defaulting to `False`) with methods `check_out()` and
`return_book()` that update `is_checked_out` and print a status message.
Create 3 `Book` objects and demonstrate checking one out and returning it.

➡️ Matching files: [`exercises/13_oop_exercises.py`](../exercises/13_oop_exercises.py) ·
[`solutions/13_oop_solutions.py`](../solutions/13_oop_solutions.py)

**Previous:** [`12-modules-and-packages`](../12-modules-and-packages/README.md) | **Next:** [`14-intermediate-python`](../14-intermediate-python/README.md)
