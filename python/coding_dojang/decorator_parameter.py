def is_multiple(x):
    def real_decorator(func):
        def wrapper(a, b):
            r = func(a, b)
            if r % x == 0:
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r
        return wrapper
    return real_decorator


@is_multiple(3)
def add(a, b):
    return a + b


print(add(10, 20))
print(add(2, 5))
