# largsfiles.py
#
# Find all transfer over a megabyte

from linesdir import lines_from_dir
from apachelog import apache_log

lines = lines_from_dir("access-log*", "www")
log = apache_log(lines)

largs = (r for r in log if r["bytes"] > 1000000)

for r in largs:
    print(r["request"], r["bytes"])
