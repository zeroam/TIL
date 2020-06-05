# genfind.py
#
# A function that generates files that match a given filename pattern

from pathlib import Path


def gen_find(filepath, top):
    yield from Path(top).rglob(filepath)


# Example use

if __name__ == "__main__":
    lognames = gen_find("access-log*", "www")
    for name in lognames:
        print(name)
