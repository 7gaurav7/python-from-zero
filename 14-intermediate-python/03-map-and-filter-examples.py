"""14 - Intermediate Python: map() and filter()"""

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda n: n * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8]


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


temps_f = list(map(celsius_to_fahrenheit, [0, 20, 37, 100]))
print(temps_f)  # [32.0, 68.0, 98.6, 212.0]

numbers = [1, 2, 3, 4, 5]
print([n * 2 for n in numbers])
print([n for n in numbers if n % 2 == 0])
