# shlex_split.py
import shlex

text = """This text has "quoted parts" inside it."""
print(f"ORIGINAL: {text!r}")
print()

print("TOKENS:")
print(shlex.split(text))
