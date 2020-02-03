def debug_transformer(func):
    def wrapper(*args, **kwargs):
        print(f'Function `{func.__name__}` called')
        # And pass it to the original function
        ret = func(*args, **kwargs)
        print(f'Function `{func.__name__}` finished')
        return ret

    return wrapper


@debug_transformer
def walkout(name):
    print(f'Bye {name}')


@debug_transformer
def get_bob():
    return 'Bob'


walkout('Felica')