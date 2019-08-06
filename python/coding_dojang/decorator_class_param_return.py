class Trace:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        r = self.func(*args, **kwargs)
        print('{0}(args={1}, kwargs={2}) -> {3})'.format(self.func.__name__, args, kwargs, r))

        return r

class Trace2:    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            r = func(*args, **kwargs)
            print('{0}(args={1}, kwargs={2}) -> {3})'.format(func.__name__, args, kwargs, r))

            return r
        return wrapper

@Trace
def add(a, b):
    return a + b

@Trace2()
def add2(a, b):
    return a + b


print(add(10, 20))
print(add(a=10, b=20))
print(add2(10, 20))
print(add2(a=10, b=20))
