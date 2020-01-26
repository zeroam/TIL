def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'in: {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def doubled(number):
    return number * 2

# Introspect
print(doubled.__name__)
print(doubled(10))