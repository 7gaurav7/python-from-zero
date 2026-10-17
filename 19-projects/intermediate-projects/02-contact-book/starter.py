"""
Intermediate Project 02 - Contact Book (starter)
Build ContactBook first with NO input()/print() inside it, then build
the menu layer around it.
"""

FILENAME = "contacts.txt"


class ContactBook:
    def __init__(self):
        self.contacts = {}  # {name: {"phone": ..., "email": ...}}

    def add_contact(self, name, phone, email):
        # TODO: validate name isn't empty, store in self.contacts
        pass

    def search_contact(self, name):
        # TODO: return the contact dict, or None if missing
        pass

    def delete_contact(self, name):
        # TODO: remove the contact; raise KeyError if missing
        pass

    def to_lines(self):
        # TODO: return a list of "name,phone,email" strings
        pass

    def load_from_lines(self, lines):
        # TODO: parse "name,phone,email" lines into self.contacts
        pass

    def save_to_file(self, filename=FILENAME):
        # TODO: write self.to_lines() to filename
        pass

    def load_from_file(self, filename=FILENAME):
        # TODO: read filename and call load_from_lines(); return True/False
        pass


def main():
    book = ContactBook()
    # TODO: load on startup, menu loop, save on quit
    pass


if __name__ == "__main__":
    main()
