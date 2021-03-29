def gen():
    print("start generator")
    a = yield 1
    print(f"a: {a}")
    print("next")
    b = yield 2 + a
    print(f"b: {b}")
    print("next")
    c = yield 3
    print(f"c: {c}")
    yield


g = gen()
print(type(g))
print(next(g))
print("-----")
print(g.send(5))
