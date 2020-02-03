def debug_transformer(func):
    def wrapper():
        print(f'Function `{func.__name__}` called')
        func()
        print(f'Function `{func.__name__}` finished')

    return wrapper


@debug_transformer
def walkout():
    print('Bye Felicia')


walkout()