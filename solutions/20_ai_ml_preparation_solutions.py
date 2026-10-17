"""
Solutions for 20 - AI/ML Preparation
Try the exercises yourself first!
(exercises/20_ai_ml_preparation_exercises.py)
Requires: pip install numpy pandas matplotlib
"""
import matplotlib
matplotlib.use("Agg")  # non-interactive backend, so this runs anywhere
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# --- 01: NumPy Fundamentals ---
numbers = np.arange(1, 11)
print(numbers.sum(), numbers.mean())

celsius = np.array([0, 10, 20, 30, 40])
fahrenheit = celsius * 9 / 5 + 32
print(fahrenheit)

scores = np.array([45, 72, 58, 91, 39])
failing = scores[scores < 60]
print(failing)

# --- 02: Pandas Fundamentals ---
students = pd.DataFrame({
    "name": ["Alice", "Bob", "Carla", "Dan"],
    "score": [95, 60, 88, 72],
})
print(students[students["score"] > 80])

# --- 03: Matplotlib Fundamentals ---
days = list(range(1, 8))
steps = [8000, 9500, 7200, 10200, 6800, 11000, 9800]

plt.figure()
plt.plot(days, steps)
plt.title("Daily Step Count")
plt.xlabel("Day")
plt.ylabel("Steps")
plt.savefig("steps_line.png")

categories = ["Reading", "Exercise", "Coding", "Sleep"]
hours = [1, 1.5, 3, 8]

plt.figure()
plt.bar(categories, hours)
plt.title("Hours Spent per Activity")
plt.savefig("activity_bar.png")
print("Charts saved.")

# --- 05: Math Foundations for ML ---
values = [4, 8, 15, 16, 23, 42]
mean = sum(values) / len(values)
variance = sum((x - mean) ** 2 for x in values) / len(values)
std_dev = variance ** 0.5
print(mean, variance, round(std_dev, 2))

arr = np.array(values)
print(arr.mean(), arr.var(), round(float(arr.std()), 2))


def linear_equation(x, slope, intercept):
    return slope * x + intercept


points = [linear_equation(x, slope=3, intercept=-2) for x in range(10)]
print(points)

# --- 06: Python Habits for AI/ML ---
raw_rows = [
    {"age": "25", "score": "90"},
    {"age": "N/A", "score": "78"},
]


def safe_float(text):
    try:
        return float(text)
    except ValueError:
        return None


cleaned_loop = []
for row in raw_rows:
    cleaned_loop.append(
        {"age": safe_float(row["age"]), "score": safe_float(row["score"])}
    )
print(cleaned_loop)


def split_dataset_70_30(data):
    split_point = int(len(data) * 0.7)
    return data[:split_point], data[split_point:]


train, test = split_dataset_70_30(list(range(10)))
print(train, test)

import os
for f in ("steps_line.png", "activity_bar.png"):
    if os.path.exists(f):
        os.remove(f)
