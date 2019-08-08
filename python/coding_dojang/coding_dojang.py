class MultipleIterator:
    def __init__(self, stop, multiple):
        self.cur = 0
        self.stop = stop
        self.multiple = multiple

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur < self.stop:
            self.cur += self.multiple
            return self.cur
        else:
            raise StopIteration


class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.cur = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur < self.stop:
            ret = self.__get_time(self.cur)
            self.cur += 1
            return ret
        else:
            raise StopIteration

    def __getitem__(self, index):
        if self.start + index < self.stop:
            return self.__get_time(self.start + index)
        else:
            raise IndexError

    def __get_time(self, second):
        hour = second // 3600 % 24
        minute = second // 60 % 60
        second = second % 60
        return '{0:02d}:{1:02d}:{2:02d}'.format(hour, minute, second)


def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1


def number_generator2():
    x = [1, 2, 3]
    yield from x
    

def three_generator():
    yield from number_generator(3)


def number_coroutine():
    try:
        while True:
            x = (yield)
            print(x, end=' ')
    
    except GeneratorExit:
        print()
        print('coroutine exit')



def sum_corouting():
    total = 0
    try:
        while True:
            x = (yield total)
            total += x
    except RuntimeError as e:
            print(e)
            yield total
    
    
co = sum_corouting()
next(co)

for i in range(20):
    co.send(i)

print(co.throw(RuntimeError, '예외로 코루틴 끝내기'))


def test(func):
    def wrapper():
        print(func.__name__, '시작')
        func()
        print(func.__name__, '끝')
    return wrapper

@test
def hello():
    print('안녕하세요')


