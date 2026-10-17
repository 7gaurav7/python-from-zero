"""
Final Project 01 - Expense Tracker (solution)

A command-line expense tracker with file persistence.
File format (CSV-like, one expense per line):
    amount,category,description
"""

FILENAME = "expenses.txt"


class Expense:
    """Represents a single expense entry."""

    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return f"${self.amount:.2f} | {self.category} | {self.description}"

    def to_line(self):
        """Serialize this expense as a single CSV-like line."""
        return f"{self.amount},{self.category},{self.description}"

    @classmethod
    def from_line(cls, line):
        """Create an Expense from a saved line of text."""
        amount_text, category, description = line.strip().split(",", 2)
        return cls(float(amount_text), category, description)


class ExpenseTracker:
    """Holds a collection of Expense objects and operations on them."""

    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        self.expenses.append(Expense(amount, category, description))

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense}")

    def total_by_category(self):
        totals = {}
        for expense in self.expenses:
            totals[expense.category] = totals.get(expense.category, 0) + expense.amount
        return totals

    def total_spent(self):
        return sum(expense.amount for expense in self.expenses)

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            print(f"Deleted: {removed}")
        else:
            print("Invalid expense number.")

    def save_to_file(self, filename=FILENAME):
        with open(filename, "w") as file:
            for expense in self.expenses:
                file.write(expense.to_line() + "\n")

    def load_from_file(self, filename=FILENAME):
        try:
            with open(filename, "r") as file:
                for line in file:
                    if line.strip():
                        self.expenses.append(Expense.from_line(line))
            print(f"Loaded {len(self.expenses)} expense(s).")
        except FileNotFoundError:
            print("No existing expense file found. Starting fresh.")


def prompt_add_expense(tracker):
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Amount must be a number.")
        return
    category = input("Category: ").strip()
    description = input("Description: ").strip()
    tracker.add_expense(amount, category, description)
    print("Expense added.")


def prompt_delete_expense(tracker):
    tracker.view_expenses()
    if not tracker.expenses:
        return
    try:
        number = int(input("Expense number to delete: "))
        tracker.delete_expense(number - 1)
    except ValueError:
        print("Please enter a valid number.")


def show_summary(tracker):
    totals = tracker.total_by_category()
    if not totals:
        print("No expenses to summarize.")
        return
    print("\n-- Spending by Category --")
    for category, total in totals.items():
        print(f"{category}: ${total:.2f}")
    print(f"\nTotal spent: ${tracker.total_spent():.2f}")


def main():
    tracker = ExpenseTracker()
    tracker.load_from_file()

    menu = (
        "\n1. Add expense\n2. View expenses\n3. Category summary"
        "\n4. Delete expense\n5. Save & Quit"
    )

    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            prompt_add_expense(tracker)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            show_summary(tracker)
        elif choice == "4":
            prompt_delete_expense(tracker)
        elif choice == "5":
            tracker.save_to_file()
            print("Expenses saved. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
