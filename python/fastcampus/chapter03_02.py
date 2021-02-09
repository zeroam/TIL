"""Dict"""
from typing import List

source = [
    ("k1", "val1"),
    ("k1", "val2"),
    ("k2", "val3"),
    ("k2", "val4"),
    ("k2", "val5"),
]

# No use setdefault
d1 = {}
for k, v in source:
    if k in d1:
        d1[k].append(v)
    else:
        d1[k] = [v]
print(d1)

# Use setdefault
d2 = {}
for k, v in source:
    d2.setdefault(k, []).append(v)
print(d2)

print()


# 사용자 정의 dict 상속(UserDict 가능)
class UserDict(dict):
    def __getitem__(self, k: str) -> List[str]:
        print(f"called: __getitem__: {k}")
        if k not in self:
            self[k] = []
        return super().__getitem__(k)

    def __setitem__(self, k: str, v: str) -> None:
        print(f"called: __setitem__: {v}")
        return super().__setitem__(k, v)


user_dict1 = UserDict(one = 1, two = 2)
user_dict2 = UserDict({"one": 1, "two": 2})
user_dict3 = UserDict([("one", 1), ("two", 2)])

print(f"user_dict1: {user_dict1}")
print(f"user_dict2: {user_dict2}")
print(f"user_dict3: {user_dict3}")

d3 = UserDict()
for k, v in source:
    d3[k].append(v)
print(d3)
print()

# Immutable dict
from types import MappingProxyType

d = {"key1": "TEST1"}
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))
print(d is d_frozen, d == d_frozen)
print()


"""Set"""
s1 = {"Apple", "Orange", "Apple", "Orange", "Kiwi"}
s2 = frozenset(s1)
print(s1, id(s1))

s1.add("Melon")
print(s1, id(s1))

try:
    s2.add("Melon")
except AttributeError:
    print("frozen set don't have add")

# 선언 최적화
from dis import dis
print(dis("{10}"))  # 좀 더 빠름
print(dis("set([10])"))
