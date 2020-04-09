# bytesgen.py
#
# An example of chaining together different generators into a processing
# pipeline.

import gzip
import bz2
import re
from pathlib import Path
from typing import List


def gen_find(filepath, top):
    yield from Path(top).rglob(filepath)


def gen_open(paths: List[Path]):
    for path in paths:
        if path.suffix == ".gz":
            yield gzip.open(path, "rt")
        elif path.suffix == ".bz2":
            yield bz2.open(path, "rt")
        else:
            yield open(path, "rt")


def gen_cat(sources):
    for src in sources:
        yield from src


def gen_grep(pat, lines):
    patc = re.compile(pat)
    return (line for line in lines if patc.search(line))


if __name__ == "__main__":
    pat = r"ply-.*\.gz"
    logdir = "www"

    filenames = gen_find("access-log*", logdir)
    logfiles = gen_open(filenames)
    loglines = gen_cat(logfiles)
    patlines = gen_grep(pat, loglines)
    bytecol = (line.rsplit(None, 1)[1] for line in patlines)
    bytes_sent = (int(x) for x in bytecol if x != "-")

    print("Total", sum(bytes_sent))
