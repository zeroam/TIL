def calc():
    result = 0
    while True:
        x, op, y = (yield result).split()
        x, y = int(x), int(y)
        if op == '+':
            result = x + y
        elif op == '-':
            result = x - y
        elif op == '*':
            result = x * y
        elif op == '/':
            result = x / y

expressions = input().split(', ')

c = calc()
next(c)

for e in expressions:
    print(c.send(e))

c.close()
