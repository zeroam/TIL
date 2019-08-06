class IsMultiple:
    def __init__(self, x):
        self.x = x

    def __call__(self, func):
        def wrapper(a, b):
            r = func(a, b)
            if r % self.x == 0:
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, self.x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, self.x))
            return r
        return wrapper


    @IsMultiple(3)
    def add(a, b):
        return a + b

    print(add(10, 20))
    print(add(2, 5))
