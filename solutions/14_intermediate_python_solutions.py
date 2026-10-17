"""
Solutions for 14 - Intermediate Python
Try the exercises yourself first! (exercises/14_intermediate_python_exercises.py)
"""

# --- 01: Comprehensions ---
cubes = [n ** 3 for n in range(1, 11)]
print(cubes)

words = ["cat", "elephant", "dog", "giraffe"]
print([w for w in words if len(w) > 4])

print({n: n ** 2 for n in range(1, 6)})

# --- 02: Lambda Functions ---
double = lambda n: n * 2
print(double(5), double(10))

people = [("Alice", 25), ("Bob", 19), ("Carla", 32)]
people.sort(key=lambda p: p[1])
print(people)

# --- 03: map() and filter() ---
numbers = [1, 2, 3, 4, 5]
print(list(map(lambda n: n ** 2, numbers)))
words = ["hi", "hello", "hey", "greetings"]
print(list(filter(lambda w: len(w) > 3, words)))


# --- 04: *args and **kwargs ---
def total(*args):
    return sum(args)


print(total(1, 2, 3, 4))


def print_all(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_all(name="Alice", age=25)

# --- 05: enumerate() and zip() ---
items = ["apple", "banana", "cherry"]
for position, item in enumerate(items, start=1):
    print(f"{position}. {item}")

names = ["Alice", "Bob"]
emails = ["alice@example.com", "bob@example.com"]
for name, email in zip(names, emails):
    print(f"{name}: {email}")

# --- 06: Unpacking ---
name, age, city = ("Alice", 25, "Paris")
print(name, age, city)

numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first, middle, last)

# --- 07: Iterators ---
items = ["a", "b", "c", "d"]
iterator = iter(items)
for _ in range(4):
    print(next(iterator))


# --- 08: Generators ---
def count_up_to(n):
    for i in range(1, n + 1):
        yield i


print(list(count_up_to(5)))


def even_numbers_up_to(n):
    for i in range(0, n + 1, 2):
        yield i


print(list(even_numbers_up_to(10)))


# --- 09: Decorators ---
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@log_calls
def say_hello():
    print("Hello!")


say_hello()


def uppercase_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


@uppercase_result
def greet(name):
    return f"hello, {name}"


print(greet("sam"))

# --- Challenges ---
words = ["fig", "kiwi", "apple", "date", "plum"]
words.sort(key=lambda w: (len(w), w))
print(words)


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fibonacci(8)))


def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    print(f"Attempt {attempt + 1} failed: {e}")
            raise last_error
        return wrapper
    return decorator


@retry(3)
def flaky_function(succeed_on_attempt, _calls=[0]):
    _calls[0] += 1
    if _calls[0] < succeed_on_attempt:
        raise ValueError("Not yet!")
    return "Success!"


print(flaky_function(2))
