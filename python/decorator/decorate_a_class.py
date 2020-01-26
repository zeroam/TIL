from real_world_example import timer


@timer
class Calculator:
    def __init__(self, num):
        self.num = num
        import time
        time.sleep(2)

    def doubled_and_add(self):
        res = sum([i * 2 for i in range(self.num)])
        print(f'Result: {res}')


c = Calculator(100)