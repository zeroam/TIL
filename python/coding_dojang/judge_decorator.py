def html_tag(tag):
    def real_decorator(func):
        def wrapper():
            r = func()
            r = f'<{tag}>{r}</{tag}>'
            return r
        return wrapper
    return real_decorator


a, b = input().split()

@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'

print(hello())
