def say_name():
    print('jayone')

def say_nationality():
    print('korea')

def say(func):
    return func

say(say_name)()
say(say_nationality)()