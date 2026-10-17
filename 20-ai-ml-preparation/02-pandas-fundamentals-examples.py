"""
20 - AI/ML Preparation: Pandas Fundamentals
Runnable examples matching the lesson.
Requires: pip install pandas
"""
import pandas as pd

# Example 1: creating a DataFrame
data = {
    "name": ["Alice", "Bob", "Carla"],
    "score": [90, 75, 88],
}
df = pd.DataFrame(data)
print(df)

# Example 2: selecting and filtering
print(df["name"])
print(df[df["score"] >= 85])

# Example 3: summary statistics
print(df["score"].mean())
print(df["score"].max())
print(df.describe())

# Example 4: grouping and aggregating
data = {
    "category": ["Food", "Food", "Transport", "Transport"],
    "amount": [20, 15, 50, 10],
}
expenses = pd.DataFrame(data)
totals = expenses.groupby("category")["amount"].sum()
print(totals)
