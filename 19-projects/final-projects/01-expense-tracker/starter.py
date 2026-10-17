"""
Final Project 01 - Expense Tracker (starter)
Build this up milestone by milestone -- see README.md.
"""

FILENAME = "expenses.txt"


class Expense:
    def __init__(self, amount, category, description):
        # TODO: store amount, category, description as attributes
        pass

    def __str__(self):
        # TODO: return a nicely formatted one-line description
        pass


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        # TODO: create an Expense and add it to self.expenses
        pass

    def view_expenses(self):
        # TODO: print every expense, numbered
        pass

    def total_by_category(self):
        # TODO: return a dict {category: total_amount}
        pass

    def total_spent(self):
        # TODO: return the sum of all expense amounts
        pass

    def delete_expense(self, index):
        # TODO: remove the expense at this index (handle bad index)
        pass

    def save_to_file(self, filename=FILENAME):
        # TODO: write all expenses to a file, one per line
        pass

    def load_from_file(self, filename=FILENAME):
        # TODO: read expenses back from a file, handling FileNotFoundError
        pass


def main():
    # TODO: menu loop tying everything together
    pass


if __name__ == "__main__":
    main()
