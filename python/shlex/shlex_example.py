# shlex_example.py
import shlex
import sys
from itertools import zip_longest

if len(sys.argv) != 2:
    print("Please specify one filename on the command line.")
    sys.exit(1)

filename = sys.argv[1]
with open(filename, "r") as f:
    body = f.read()
print(f"ORIGINAL: {body!r}")
print()

word_size = 25
print(f"TOKENS:")
print(f"|{'shlex':^{word_size}}|{'str':^{word_size}}|")
print("-" * (word_size * 2 + 3))
lexer = shlex.shlex(body)
str_split = str.split(body)

for token, token_str in zip_longest(lexer, str_split):
    print(f"|{token!r:{word_size}}|{token_str!r:{word_size}}|")
