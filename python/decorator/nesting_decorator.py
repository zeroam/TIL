def hello(func):
    def wrapper():
        print('Hello')
        func()
    return wrapper


def welcome(func):
    def wrapper():
        print('Welcome')
        func()
    return wrapper


@hello
@welcome
def say():
    print('Greeting Dome')

say()