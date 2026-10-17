# Beginner Project 02 — Simple Calculator

## 1. Problem Statement
Build a command-line calculator that repeatedly asks for two numbers and
an operator, performs the calculation, and prints the result — without
crashing on bad input.

## 2. Learning Objectives
- Writing a pure function that returns a value instead of printing directly
- Branching on an operator with `if`/`elif`/`else`
- Handling multiple exception types (`ValueError`, `ZeroDivisionError`)
- Structuring a "calculate again?" loop

## 3. Requirements
- Support `+`, `-`, `*`, `/`.
- One function, `calculate(a, b, operator)`, returns the result or raises
  an appropriate exception.
- Handle invalid numbers and division by zero.
- Loop until the user chooses to quit.

## 4. Features
- [ ] Supports all four basic operators
- [ ] Rejects unknown operators with a clear error
- [ ] Handles non-numeric input without crashing
- [ ] Handles division by zero without crashing
- [ ] Loops until the user chooses to stop

## 5. Suggested Folder Structure
```
02-simple-calculator/
├── README.md
├── starter.py
├── tests/test_calculator.py
└── solution/solution.py
```

## 6. Step-by-Step Milestones
1. Write `calculate(a, b, operator)` for `+ - * /`, raising `ValueError`
   for an unknown operator.
2. Wire it up to `input()` for one calculation.
3. Add `try`/`except` around conversion and calculation.
4. Wrap in a loop with a "calculate again?" prompt.

## 7. Starter Code
See [`starter.py`](starter.py).

## 8. Test Cases
See [`tests/test_calculator.py`](tests/test_calculator.py). Run with:
```
python -m unittest tests.test_calculator
```

## 9. Expected Behavior
```
Simple Calculator — supported operators: + - * /
First number: 10
Operator (+ - * /): /
Second number: 4
Result: 2.5
Calculate again? (y/n): n
Goodbye!
```

## 10. Extension Challenges
- Add `**` and `%`.
- Keep a running history of calculations.
- Round float results to 2 decimal places for display.

## 11. Solution
See [`solution/solution.py`](solution/solution.py). Attempt `starter.py` first.

**Related lessons:** [`09-functions`](../../../09-functions/README.md),
[`03-operators`](../../../03-operators/README.md),
[`11-exceptions`](../../../11-exceptions/README.md).
