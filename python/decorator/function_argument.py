def say_hello(name):
    print(f'Hello, {name}')


def say_goodbye(name):
    print(f'Goodbye, {name}')


def say_to_bob(func):
    func('Bob')


say_to_bob(say_hello)
say_to_bob(say_goodbye)