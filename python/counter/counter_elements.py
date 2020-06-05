import collections

c = collections.Counter("extremely")
c["z"] = 0

print(c)
print(list(c.elements()))

print("Most common:")
for letter, count in c.most_common(3):
    print(f"{letter}:{count:7d}")
