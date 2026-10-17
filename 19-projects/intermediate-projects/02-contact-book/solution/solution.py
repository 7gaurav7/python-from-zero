"""
Intermediate Project 02 - Contact Book (solution)

ContactBook holds the data and pure logic (add/search/delete plus
serializing to and from plain text lines), with no input()/print() of
its own -- see tests/test_contacts.py.
"""

FILENAME = "contacts.txt"


class ContactBook:
    def __init__(self):
        self.contacts = {}  # {name: {"phone": ..., "email": ...}}

    def add_contact(self, name, phone, email):
        name = name.strip()
        if not name:
            raise ValueError("Name can't be empty.")
        self.contacts[name] = {"phone": phone.strip(), "email": email.strip()}

    def search_contact(self, name):
        return self.contacts.get(name)

    def delete_contact(self, name):
        if name not in self.contacts:
            raise KeyError(f"No contact named '{name}'.")
        del self.contacts[name]

    def to_lines(self):
        return [
            f"{name},{info['phone']},{info['email']}"
            for name, info in self.contacts.items()
        ]

    def load_from_lines(self, lines):
        for line in lines:
            line = line.strip()
            if not line:
                continue
            name, phone, email = line.split(",")
            self.contacts[name] = {"phone": phone, "email": email}

    def save_to_file(self, filename=FILENAME):
        with open(filename, "w") as file:
            for line in self.to_lines():
                file.write(line + "\n")

    def load_from_file(self, filename=FILENAME):
        try:
            with open(filename, "r") as file:
                self.load_from_lines(file)
            return True
        except FileNotFoundError:
            return False


def prompt_add(book):
    try:
        book.add_contact(input("Name: "), input("Phone: "), input("Email: "))
        print("Contact added.")
    except ValueError as e:
        print(e)


def print_all(book):
    if not book.contacts:
        print("No contacts saved yet.")
        return
    for name, info in book.contacts.items():
        print(f"{name}: {info['phone']} | {info['email']}")


def prompt_search(book):
    info = book.search_contact(input("Name to search: ").strip())
    print(info if info else "Contact not found.")


def prompt_delete(book):
    try:
        book.delete_contact(input("Name to delete: ").strip())
        print("Deleted.")
    except KeyError as e:
        print(e)


def main():
    book = ContactBook()
    if book.load_from_file():
        print(f"Loaded {len(book.contacts)} contact(s).")
    else:
        print("No existing contact file found. Starting fresh.")

    actions = {
        "1": lambda: prompt_add(book),
        "2": lambda: print_all(book),
        "3": lambda: prompt_search(book),
        "4": lambda: prompt_delete(book),
    }
    while True:
        print("\n1. Add  2. View all  3. Search  4. Delete  5. Save & Quit")
        choice = input("Choose an option: ").strip()
        if choice == "5":
            book.save_to_file()
            print("Contacts saved. Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
