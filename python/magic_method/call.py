class MyClass(object):

    def __init__(self, var_one, var_two, var_three):
        self.var_1 = var_one
        self.var_2 = var_two
        self.var_3 = var_three

    def __call__(self, *vars):
        self.var_1, self.var_2 = vars


if __name__ == '__main__':
    obj = MyClass(1, 2, 3)

    print(obj.__dict__)
    print(id(obj), '\n')

    # Now, let's change the objects state
    obj(200, 300)

    print(obj.__dict__)
    print(id(obj), '\n')