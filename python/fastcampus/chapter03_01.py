import array

"""List Comprehension"""
chars = "!@#$%^&*()_+"

# create list
l1 = [ord(char) for char in chars]
# create list + filter
l2 = [ord(char) for char in chars if ord(char) > 40]
# create generator
l3 = (ord(char) for char in chars)

print(l1)
print(l2)
print(l3)
print()

"""Array"""
arr = array.array("I", (ord(s) for s in chars))

print(f"array: {arr}")
print(f"array to list: {arr.tolist()}")
print()


# 리스트 주의할 점
marks1 = [[0] * 3 for _ in range(3)]
marks2 = [[0] * 3] * 3

marks1[0][1] = 3
marks2[0][1] = 3

print(marks1)
print([id(mark) for mark in marks1])
print(marks2)
print([id(mark) for mark in marks2])
print()


"""Mutable vs Imutable"""
t = (10, 15, 20)
l = [10, 15, 20]
print(id(t), id(l))

t = t * 2
l = l * 2  # 리스트를 새로 생성
print(id(t), id(l))

t *= 2
l *= 2  # 기존 리스트에서 extend
print(id(t), id(l))
print()
