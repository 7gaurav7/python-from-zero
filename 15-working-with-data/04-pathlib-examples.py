"""15 - Working with Data: pathlib
Creates 'note.txt' in this folder when run."""
from pathlib import Path

file_path = Path("data") / "students.csv"
print(file_path)

file_path = Path("data/students.csv")
print(file_path.name)
print(file_path.stem)
print(file_path.suffix)
print(file_path.parent)

note_path = Path("note.txt")
note_path.write_text("Remember to practice Python today!")
print(note_path.read_text())

folder = Path(".")
print(folder.exists())
print(len(list(folder.glob("*.py"))) >= 0)
