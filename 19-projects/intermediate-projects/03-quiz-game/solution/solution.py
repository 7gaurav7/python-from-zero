"""
Intermediate Project 03 - Quiz Game (solution)

grade_answer() is a pure function (no input()/print()) so it can be
tested directly -- see tests/test_quiz.py.
"""

QUESTIONS = [
    {
        "question": "What does CPU stand for?",
        "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit"],
        "answer": "Central Processing Unit",
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["func", "def", "function"],
        "answer": "def",
    },
    {
        "question": "What data type is the result of 5 / 2 in Python 3?",
        "options": ["int", "float", "str"],
        "answer": "float",
    },
]


def grade_answer(question_data, choice):
    options = question_data["options"]
    if not (1 <= choice <= len(options)):
        return False
    return options[choice - 1] == question_data["answer"]


def ask_question(question_data):
    print("\n" + question_data["question"])
    for i, option in enumerate(question_data["options"], start=1):
        print(f"  {i}. {option}")

    try:
        choice = int(input("Your answer (number): "))
    except ValueError:
        print("Invalid choice, marking as incorrect.")
        return False

    correct = grade_answer(question_data, choice)
    if correct:
        print("Correct!")
    else:
        print(f"Incorrect. The right answer was: {question_data['answer']}")
    return correct


def run_quiz():
    score = 0
    for question_data in QUESTIONS:
        if ask_question(question_data):
            score += 1

    total = len(QUESTIONS)
    print(f"\nYou got {score}/{total} correct!")

    if score == total:
        print("Perfect score!")
    elif score >= total / 2:
        print("Good job!")
    else:
        print("Keep practicing!")


if __name__ == "__main__":
    run_quiz()
