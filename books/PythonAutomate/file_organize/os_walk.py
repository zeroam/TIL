import os
from pathlib import Path

sample = Path.home() / 'Documents' / 'Python Scripts'
print(sample)
for curfolder, subfolders, filenames in os.walk(sample):
    print("The current folder is " + curfolder)

    for subfolder in subfolders:
        print(f"  subfolder of {curfolder} : {subfolder}")

    for filename in filenames:
        print(f"  file inside {curfolder} : {filename}")

print()
