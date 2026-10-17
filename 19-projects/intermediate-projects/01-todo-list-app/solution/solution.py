"""
Intermediate Project 01 - To-Do List App (solution)

The task-management logic lives in the TaskManager class, which has no
input()/print() calls of its own -- that separation makes it easy to
unit test (see tests/test_todo.py).
"""

FILENAME = "tasks.txt"


class TaskManager:
    def __init__(self):
        self.tasks = []  # each task: {"text": "...", "done": False}

    def add_task(self, text):
        text = text.strip()
        if not text:
            raise ValueError("Task description can't be empty.")
        self.tasks.append({"text": text, "done": False})

    def list_tasks(self):
        return list(self.tasks)

    def complete_task(self, index):
        if not (0 <= index < len(self.tasks)):
            raise IndexError("That task number doesn't exist.")
        self.tasks[index]["done"] = True

    def remove_task(self, index):
        if not (0 <= index < len(self.tasks)):
            raise IndexError("That task number doesn't exist.")
        return self.tasks.pop(index)


def show_menu():
    print("\n1. Add task\n2. View tasks\n3. Mark complete\n4. Remove task\n5. Quit")


def print_tasks(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{i}. {status} {task['text']}")


def prompt_add(manager):
    try:
        manager.add_task(input("Task description: "))
        print("Task added.")
    except ValueError as e:
        print(e)


def prompt_select_index(manager):
    print_tasks(manager)
    if not manager.list_tasks():
        return None
    try:
        number = int(input("Task number: "))
        return number - 1
    except ValueError:
        print("Please enter a valid number.")
        return None


def prompt_complete(manager):
    index = prompt_select_index(manager)
    if index is None:
        return
    try:
        manager.complete_task(index)
        print("Task marked complete.")
    except IndexError as e:
        print(e)


def prompt_remove(manager):
    index = prompt_select_index(manager)
    if index is None:
        return
    try:
        removed = manager.remove_task(index)
        print(f"Removed: {removed['text']}")
    except IndexError as e:
        print(e)


def main():
    manager = TaskManager()
    actions = {
        "1": lambda: prompt_add(manager),
        "2": lambda: print_tasks(manager),
        "3": lambda: prompt_complete(manager),
        "4": lambda: prompt_remove(manager),
    }
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
