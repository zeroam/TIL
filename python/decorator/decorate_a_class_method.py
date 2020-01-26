from real_world_example import timer


class Calculator:
    def __init__(self, num):
        self.num = num

    @timer
    def doubled_and_add(self):
        res = sum([i * 2 for i in range(self.num)])
        print(f"Result : {res}")


c = Calculator(10000)
c.doubled_and_add()