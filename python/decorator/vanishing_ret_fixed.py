def debug_transformer(func):
    def wrapper():
        print(f'Function `{func.__name__}` called')
        ret = func()
        print(f'Function `{func.__name__}` finished')
        return ret

    return wrapper


@debug_transformer
def walkout():
    print('Bye Felical')


@debug_transformer
def get_bob():
    return 'Bob'


bob = get_bob()
print(bob)