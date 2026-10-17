"""
20 - AI/ML Preparation: Matplotlib Fundamentals
Runnable examples matching the lesson.
Requires: pip install matplotlib pandas
Running this script saves several .png chart files in this folder.
"""
import matplotlib
matplotlib.use("Agg")  # non-interactive backend so this runs without a display
import matplotlib.pyplot as plt
import pandas as pd

# Example 1: a basic line plot
days = [1, 2, 3, 4, 5]
temperatures = [15, 17, 16, 19, 21]

plt.figure()
plt.plot(days, temperatures)
plt.title("Temperature Over 5 Days")
plt.xlabel("Day")
plt.ylabel("Temperature (C)")
plt.savefig("temperature_line.png")
print("Chart saved.")

# Example 2: a bar chart
categories = ["Food", "Transport", "Entertainment"]
amounts = [150, 60, 40]

plt.figure()
plt.bar(categories, amounts)
plt.title("Spending by Category")
plt.ylabel("Amount ($)")
plt.savefig("spending_bar.png")
print("Chart saved.")

# Example 3: multiple lines with a legend
city_a = [15, 17, 16, 19, 21]
city_b = [10, 11, 14, 13, 12]

plt.figure()
plt.plot(days, city_a, label="City A")
plt.plot(days, city_b, label="City B")
plt.title("Temperature Comparison")
plt.xlabel("Day")
plt.ylabel("Temperature (C)")
plt.legend()
plt.savefig("comparison_line.png")
print("Chart saved.")

# Example 4: plotting directly from a pandas DataFrame
data = {"category": ["Food", "Transport", "Fun"], "amount": [150, 60, 40]}
df = pd.DataFrame(data)

plt.figure()
plt.bar(df["category"], df["amount"])
plt.title("Spending by Category (from a DataFrame)")
plt.savefig("df_spending_bar.png")
print("Chart saved.")
