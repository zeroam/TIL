def say_hello(name):
    print(f'Hello, {name}')


def say_goodbye(name):
    print(f'Goodbye, {name}')


def get_greeting(greeting):
    if greeting == 'hello':
        greeting_func = say_hello
    elif greeting == 'goodbye':
        greeting_func = say_goodbye

    return greeting_func


def say_to_bob(greeting):
    greeting_func = get_greeting(greeting)
    greeting_func('Bob')


say_to_bob('hello')
say_to_bob('goodbye')