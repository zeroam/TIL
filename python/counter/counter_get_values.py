import collections

c = collections.Counter("abcdaab")

for letter in "abcde":
    print(f"{letter} : {c[letter]}")
