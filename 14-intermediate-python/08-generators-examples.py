"""14 - Intermediate Python: Generators"""


def countdown(n):
    while n > 0:
        yield n
        n -= 1


for number in countdown(3):
    print(number)


def numbers_generator():
    print("Starting...")
    yield 1
    print("About to yield 2...")
    yield 2


gen = numbers_generator()
print("Generator created.")
for n in gen:
    print(n)

squares = (n ** 2 for n in range(1, 6))
print(list(squares))


def even_numbers():
    n = 0
    while True:
        yield n
        n += 2


gen = even_numbers()
print([next(gen) for _ in range(5)])
