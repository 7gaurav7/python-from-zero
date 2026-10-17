"""14 - Intermediate Python: Decorators"""
import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.6f} seconds")
        return result
    return wrapper


@time_it
def slow_add(a, b):
    time.sleep(0.1)
    return a + b


print(slow_add(2, 3))


def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@log_calls
def add(a, b):
    return a + b


print(add(3, 4))


def shout(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


def greet(name):
    return f"hello, {name}"


greet = shout(greet)
print(greet("alice"))


def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def say_hi():
    print("Hi!")


say_hi()
