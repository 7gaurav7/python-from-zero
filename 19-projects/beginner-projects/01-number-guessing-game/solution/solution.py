"""
Beginner Project 01 - Number Guessing Game (solution)

The core comparison logic is pulled out into check_guess() so it can be
tested without needing to simulate keyboard input -- see tests/test_game.py.
"""
import random


def check_guess(secret_number, guess):
    """Compare a guess to the secret number.

    Returns one of: "too_low", "too_high", "correct".
    This function has no input()/print() calls, which makes it easy to
    unit test in isolation.
    """
    if guess < secret_number:
        return "too_low"
    elif guess > secret_number:
        return "too_high"
    else:
        return "correct"


def play_game(max_attempts=None):
    secret_number = random.randint(1, 100)
    guesses = 0

    print("I'm thinking of a number between 1 and 100.")

    while True:
        if max_attempts is not None and guesses >= max_attempts:
            print(f"Out of attempts! The number was {secret_number}.")
            break

        guess_text = input("Your guess: ")
        try:
            guess = int(guess_text)
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        guesses += 1
        result = check_guess(secret_number, guess)

        if result == "too_low":
            print("Too low!")
        elif result == "too_high":
            print("Too high!")
        else:
            print(f"Correct! You got it in {guesses} guesses.")
            break


if __name__ == "__main__":
    play_game()
