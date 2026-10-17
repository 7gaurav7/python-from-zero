# Beginner Project 01 — Number Guessing Game

## 1. Problem Statement
Build a command-line game where the computer secretly picks a random
number between 1 and 100. The player repeatedly guesses until they find
it, receiving a "Too high!" or "Too low!" hint after every wrong guess.

## 2. Learning Objectives
- Generating random numbers with the `random` module
- Controlling repetition with a `while` loop
- Branching logic with `if`/`elif`/`else`
- Validating user input with `try`/`except`
- Structuring a small program around one clear function per responsibility

## 3. Requirements
- Use `random.randint(1, 100)` to pick the secret number.
- Loop until the player guesses correctly.
- After each wrong guess, print `"Too high!"` or `"Too low!"`.
- Count and display the number of guesses once the player wins.
- Handle non-numeric input without crashing.

## 4. Features
- [ ] Random secret number each run
- [ ] Clear high/low feedback after every guess
- [ ] Final guess count shown on a win
- [ ] Graceful handling of invalid (non-numeric) input
- [ ] (Stretch) Optional maximum number of attempts

## 5. Suggested Folder Structure
```
01-number-guessing-game/
├── README.md
├── starter.py
├── tests/test_game.py
└── solution/solution.py
```

## 6. Step-by-Step Milestones
1. Pick a random number and let the player guess exactly once.
2. Wrap the guess in a `while` loop so the player keeps guessing.
3. Count guesses and announce the count on a win.
4. Add `try`/`except` for non-numeric guesses.
5. (Stretch) Add an optional maximum number of attempts.

## 7. Starter Code
See [`starter.py`](starter.py).

## 8. Test Cases
See [`tests/test_game.py`](tests/test_game.py) — tests the pure
`check_guess(secret_number, guess)` function. Run with:
```
python -m unittest tests.test_game
```

## 9. Expected Behavior
```
I'm thinking of a number between 1 and 100.
Your guess: 50
Too high!
Your guess: 25
Too low!
Your guess: 37
Correct! You got it in 3 guesses.
```

## 10. Extension Challenges
- Let the player choose the guessing range.
- Add a "play again?" loop.
- Give a "warmer/colder" hint based on distance from the previous guess.

## 11. Solution
See [`solution/solution.py`](solution/solution.py). Attempt `starter.py` first.

**Related lessons:** [`05-loops`](../../../05-loops/README.md),
[`04-conditions`](../../../04-conditions/README.md),
[`11-exceptions`](../../../11-exceptions/README.md).
