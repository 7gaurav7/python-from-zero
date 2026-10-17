"""14 - Intermediate Python: *args and **kwargs"""


def total(*args):
    return sum(args)


print(total(1, 2, 3))
print(total(10, 20))


def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


describe_person(name="Alice", age=25, city="Paris")


def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")


greet("Hello", "Alice", "Bob", "Carla")


def add(a, b, c):
    return a + b + c


print(add(*[1, 2, 3]))
print(add(**{"a": 10, "b": 20, "c": 30}))
