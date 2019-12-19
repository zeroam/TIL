from pathlib import Path

path = Path('names.txt')
path.touch()

path.rename('mynames.txt')