# Intermediate Project 03 — Quiz Game

## 1. Problem Statement
Build a multiple-choice quiz game that asks a series of questions, tracks
the score, and shows a final result with performance-based feedback.

## 2. Learning Objectives
- Modeling questions as a list of dictionaries
- Separating "is this answer correct?" logic from `input()`/`print()`
- Looping while tracking running state (the score)
- Giving different feedback based on a final computed value

## 3. Requirements
- Store questions as dictionaries with `question`, `options`, `answer`.
- Display each question's numbered options.
- Track correct answers and print a final score summary.
- Treat invalid/out-of-range choices as incorrect, not a crash.

## 4. Features
- [ ] Displays each question with numbered options
- [ ] Grades each answer correctly, including invalid choices
- [ ] Tracks and displays a final score
- [ ] Gives different feedback for perfect/good/weak performance
- [ ] (Stretch) Loads questions from an external file

## 5. Suggested Folder Structure
```
03-quiz-game/
├── README.md
├── starter.py
├── tests/test_quiz.py
└── solution/solution.py
```

## 6. Step-by-Step Milestones
1. Write pure `grade_answer(question_data, choice)`.
2. Write `ask_question()` using `grade_answer()`.
3. Loop through all questions in `run_quiz()`, tracking the score.
4. Add performance-based feedback messages.

## 7. Starter Code
See [`starter.py`](starter.py).

## 8. Test Cases
See [`tests/test_quiz.py`](tests/test_quiz.py). Run with:
```
python -m unittest tests.test_quiz
```

## 9. Expected Behavior
```
What does CPU stand for?
  1. Central Process Unit
  2. Central Processing Unit
  3. Computer Personal Unit
Your answer (number): 2
Correct!
...
You got 3/3 correct!
Perfect score!
```

## 10. Extension Challenges
- Load questions from JSON/CSV (see `15-working-with-data`).
- Shuffle questions/options with `random.shuffle()`.
- Add a difficulty level.

## 11. Solution
See [`solution/solution.py`](solution/solution.py). Attempt `starter.py` first.

**Related lessons:** [`08-dictionaries`](../../../08-dictionaries/README.md),
[`05-loops`](../../../05-loops/README.md),
[`09-functions`](../../../09-functions/README.md).
