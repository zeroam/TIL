def say(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@say
def greet(name):
    print(f'Hello {name}')


greet('jayone')