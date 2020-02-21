from inspect import getfullargspec


class Function(object):
    """Function is a wrap over standard python function
    """
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        """Overriding the __call__ function which makes the 
        instance callable
        """
        # fetching the function to be invoked from the virtual namespace
        # through the arguments
        fn = Namespace.get_instance().get(self.fn, *args)
        if not fn:
            raise Exception('no matching function found.')

        # invoking the wrapped function and returning the value
        return fn(*args, **kwargs)

    def key(self, args=None):
        """Returns the key that will uniquely identify
        a function (even when it is overloaded)
        """
        # if args not specified, extract the arguments from the
        # function definition
        if args is None:
            args = getfullargspec(self.fn).args

        return tuple([
            self.fn.__module__,
            self.fn.__class__,
            self.fn.__name__,
            len(args or []),
        ])


class Namespace(object):
    """Namespace is the singleton class that is responsible
    for holding all the functions.
    """
    __instance = None

    def __init__(self):
        if self.__instance is None:
            self.function_map = dict()
            Namespace.__instance = self
        else:
            raise Exception('cannot instantiate a virtual Namespace again')

    @staticmethod
    def get_instance():
        if Namespace.__instance is None:
            Namespace()
        return Namespace.__instance

    def register(self, fn):
        """registers the function in the virtual namespace and returns
        an instance of callable Function that wraps the 
        function fn
        """
        func = Function(fn)
        self.function_map[func.key()] = fn
        return func

    def get(self, fn, *args):
        """get returns the matching function from the virtual namespace.

        return None if it did not fund any matching function.
        """
        func = Function(fn)
        return self.function_map.get(func.key(args=args))


def overload(fn):
    """overload is the decorator that wraps the function
    and returns a callable object of type Function.
    """
    return Namespace.get_instance().register(fn)


if __name__ == '__main__':
    @overload
    def area(l, b):
        return l * b

    @overload
    def area(r):
        import math
        return math.pi * r ** 2

    print(area(3, 4))
    print(area(7))
    print(locals())
