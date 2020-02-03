def walkout():
    print('Bye Felicia')


def debug_transformer(func):
    def wrapper():
        print(f'Function `{func.__name__}` called')
        func()
        print(f'Function `{func.__name__}` finished')

    return wrapper


walkout = debug_transformer(walkout)
walkout()