"""
Intermediate Project 03 - Quiz Game (starter)
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
    # TODO: return True/False for whether 1-based `choice` is correct.
    # An out-of-range choice should count as False, not raise an error.
    pass


def ask_question(question_data):
    # TODO: print question/options, read the answer, use grade_answer(),
    # print feedback, return True/False
    pass


def run_quiz():
    # TODO: loop through QUESTIONS, track score, print a final summary
    pass


if __name__ == "__main__":
    run_quiz()
