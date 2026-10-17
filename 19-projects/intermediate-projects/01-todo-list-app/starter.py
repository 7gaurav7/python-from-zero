"""
Intermediate Project 01 - To-Do List App (starter)

Build the TaskManager class first with NO input()/print() calls inside
it -- that's what makes it testable. Then build the input/output layer.
"""

FILENAME = "tasks.txt"


class TaskManager:
    def __init__(self):
        self.tasks = []  # each task: {"text": "...", "done": False}

    def add_task(self, text):
        # TODO: strip text, raise ValueError if empty, else append a task
        pass

    def list_tasks(self):
        # TODO: return the list of tasks
        pass

    def complete_task(self, index):
        # TODO: mark tasks[index] as done; raise IndexError if out of range
        pass

    def remove_task(self, index):
        # TODO: remove and return tasks[index]; raise IndexError if out of range
        pass


def show_menu():
    print("\n1. Add task\n2. View tasks\n3. Mark complete\n4. Remove task\n5. Quit")


def main():
    manager = TaskManager()
    # TODO: menu loop calling manager's methods and printing feedback
    pass


if __name__ == "__main__":
    main()
