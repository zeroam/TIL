from pathlib import Path

path = Path('words.txt')

contents = path.read_text()
print(contents)