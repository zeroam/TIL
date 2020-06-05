import pickle


class foobar:
    def __init__(self):
        self.a = 35
        self.b = "test"
        self.c = lambda x: x * x

    def __getstate__(self):
        attributes = self.__dict__.copy()
        del attributes["c"]
        return attributes

    def __setstate__(self, state):
        self.__dict__ = state
        self.c = lambda x: x * x


my_foobar_instance = foobar()
my_pickle_string = pickle.dumps(my_foobar_instance)
my_new_instance = pickle.loads(my_pickle_string)
print(my_new_instance.__dict__)
print(my_new_instance.c(5))
