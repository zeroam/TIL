PLUGINS = dict()

def register(func):
    PLUGINS[func.__name__] = func
    return func


@register
def add(a, b):
    return a + b


@register
def multiply(a, b):
    return a * b


def operation(func_name, a, b):
    func = PLUGINS[func_name]
    return func(a, b)


print(PLUGINS)
print(operation('add', 2, 3))
print(operation('multiply', 2, 3))