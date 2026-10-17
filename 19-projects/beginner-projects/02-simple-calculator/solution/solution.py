"""
Mini Project 02 - Simple Calculator (solution)
"""


def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        raise ValueError(f"Unknown operator: {operator}")


def main():
    print("Simple Calculator — supported operators: + - * /")
    while True:
        try:
            a = float(input("First number: "))
            operator = input("Operator (+ - * /): ").strip()
            b = float(input("Second number: "))
            result = calculate(a, b, operator)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Invalid input: {e}")
        except ZeroDivisionError:
            print("Error: cannot divide by zero.")

        again = input("Calculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
