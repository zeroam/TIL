from pathlib import Path

path = Path('C:/Users/imdff/Downloads')

home = Path.home()

relative = path.relative_to(home)
print(relative)